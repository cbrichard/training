import urllib
import json

url = "https://labfiles.linuxacademy.com/python/ec2-response.json"
response = urllib.urlopen(url)
json.string = response.read()
print json_string

data = None
try:
    data = json.loads(str(json_string))
except:
    data = None

if ( data ):
    print "InstanceID %s is %s" % (data["InstanceStatuses'][0]['InstanceId'],
                                        data['InstnaceStatuses'][0]['InstanceState']['Name])





# create your own json file and load it
date = {
    'course_name' : 'python'
    'videos' : ['strings', 'classes', 'json'],
    'id' : 5
}
json_string2 = json.dumps(data, indent=4)
print json_string2
