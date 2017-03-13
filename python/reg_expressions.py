line = 'Oct 7 17:28:59 kiri sshd[2355]: Failed password for root from 32.555.7.45 port 57984 ssh2'

import re

#match = re.search('sshd', line)

#print match


# Using a regex

match = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w*\ssshd\[\d*\]: Failed password for \w+ \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2', line)


# Simplified regex
match =  re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$', line)
print match.groups()

print match.group(1)
print match.group(2)
print match.group(3)


