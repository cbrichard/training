import time
import urllib2

def download_webpage():
    url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
    response = urllib2.urlopen(url, timeout = 60)
    return response.read()

def elapsed_time():
    t0 = time.time()
    webpage = download_webpage()
    t1 = time.time()
    print "Elapsed time: %s\n" % (t1 - t0)

# Call function to time webpage download
elapsed_time()


# elapse time function as a decorator

def elapsed_time2(funtion_to_time):
    def wrapper():
        t0 = time.time()
        function_to_time()
        t1 = time.time()
        print "Elapsed time: %s\n" % (t1 - t0)
    return wrapper

# Now create the download webpage function with the decorator for elapse_time

@elapsed_time2
def download_webpage2():
    url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
    response = urllib2.urlopen(url, timeout = 60)
    return response.read()

webpage = download_webpage2()
