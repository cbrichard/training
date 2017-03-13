import subprocess

lookup_user = 'kiri'

def activeProcesses1(lookup_user):
    processes_running = 0
    for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
        user = line.split()[0]
        if lookup_user == user:
            processes_running+1
    return "User %s has %s processes running" % (lookup_user, processes_running)

print activeProcesses1(lookup_user)

def activeProcesses2(lookup_user, lookup_cmd):
    processes_running_all = 0
    processes_running_searched = 0
    for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
        user = line.split()[0]
        if lookup_user == user:
            processes_running_all+=1
            if lookup_cmd in line:
                processes_running_searched+=1
    return processes_running_all, processes_running_searched

procs_total, procs_searched = activeProcesses2('kiri', 'bash')
print procs_total, procs_searched
