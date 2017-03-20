#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List comprehension, create a dict from user in /etc/passwd

#d = dict([(line.split(':')[0], line.split(':')[4])
#          for line in open('/etc/passwd').readlines() if not line.startswith('#')])
#
#for k, v in sorted(d.items()):
#    print(k, v)



# Or you can do it this way
users = {}
with open('/etc/passwd') as f:
    for line in f:
        if not line.startswith("#"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[4]

for username in sorted(users):
    print "User: %s   Description: %s" % (username, users[username])
