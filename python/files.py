filename = '/var/log/system.log'

for line in open(filename):
    print line

# or

with open(filename)as file_handle:
    lines = file_handle.readlines()
    for line in lines:
        print(line)

# Write to files

filename2 = 'textfile.txt'

with open(filename2, 'w') as file_handle2:
    file_handle2.write("here is some text\n")

with open(filename2, 'a') as file_handle2:
    file_handle2.write("here is more text")


# Useing csv

import csv
file_handle = open('servers.csv')
reader = csv.reader(file_handle)
os_counts = {}
for row in reader:
    os_counts[row[2]] = os_counts.get(row[2],0)+1

print os_counts


