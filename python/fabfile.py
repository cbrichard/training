from fabric.api import sudo

def UpdateServer():
    sudo("apt-get update && apt-get upgrade -y ", pty=True)

""" This example uses Python Fabric to deploy MySQL/MariaDB and Apache on five servers """

# import the os module to get file basenames
import os

# define groups of webservers and databases

env.roledefs = {
    "webserver" : [ "ip1", "ip2", "ip3" ],
    "databases" : [ "ip1", "ip2" ],
}

# define a special group called all so we can easily send out commands to all servers if needed
env.roledefs["all"] = [ h for r in env.roledefs.values() for h in r ]

# the packages that are required to run our applications on the server groups
packages_required = {
    "webserver" : [    "httpd","php","ntp","php-mysqli"],
    "databases" : [ "mariadb-server" ]

# files that need to be downloaded from the labserver repo
download_files = {
    "database" : ["http://labfiles.linuxacademy.com/python/fabric/sakila.sql",
                  "http://labfiles.linuxacademy.com/python/fabric/sakila-data.sql"],
    "webserver" : ["http://labfiles.linuxacademy.com/python/fabric/index.php"]
}

@roles("database") # this decorator will make the function following it run for all database servers
    def install_databases():
    # install the database application
    # sudo is used when you need to run a cmd on the remote server as superuser
    sudo("yum -y install %s" % " ".join(packages_required["database"]),pty=True)

    # active MySQL/MariaDB in system control
    sudo("systemctl enable mariadb",pty=True)

    # start MySQL/MariaDB using the system control
    sudo("systemctl start mariadb",pty=True)

    # Create a user on the database that we will be using from our webservers
    sudo(r""" mysql -h 127.0.0.1 -u root -e "CREATE USER 'web'@'%'  IDENTIFIED BY 'web'; GRANT ALL
         PRIVILEGES ON *.* TO 'web'@'%'; FLUSH PRIVILEGES; "   """ )
    # Check for the mysql process is running
    # This is how you run a a command when you do not need super user
    run("ps -ef | grep mysql")

    @parallel
    @roles("database") # this decorator will ake the function following it run for all databases
    def setup_database():
        # Setup the tmp directory where we will download files from the web
        tmpdir = "/tmp"

        # this cd is the fabric command to change directory on the remote server
        with cd(tmpdir):
            # iterate over the files we need to download for the database
            for url in download_files["database"]:
            # basename gives us just the name of the file, without any path info, it also works for
            # urls
            filename = "%s/%s" %(tmpdir, os.path.basename(url));
            
            # using the function run on the remote server, we can execute commmands, in this case
            # wget which opens the url and save it to the filename
            run("wget --no-cache %s -O %s" % (url, filename)

            # since these are SQL files, we can just dump them into out MySQL/MariaDB server
            run("mysql -u root < %s" % filename)

@roles("webserver")
def install_webserver():
    # install the webserver applications
    sudo("yum -y install %s" % " ".join(packages_required["webserver"]),pty=True)

    sudo("systemctl enable httpd.service", pty=True)
    sudo("systemctl start httpd.service", pty=True)


    sudo("setsebool -P httpd_can_network_connect=1", pty=True)
    sudo("setsebook -P httpd_read_user_content=1", pty=True)

@roles("webserver")
def setup_webserver():

