import subprocess


# Global Variable

partition_usage_threshold = 5

df_cmd = subprocess.check_output(['df','-k'])

lines = df_cmd.splitlines()

for line in lines[1:]:
    columns = line.split()
    used_percentage = columns[4]
    used_percentage = used_percentage.replace('%','')
    if int(used_percentage) >= partition_usage_threshold:
           print "partition %s usage is beyond threshold at %s " % (columns[0], columns[4])
           # you can have an email function here that alerts you about this


