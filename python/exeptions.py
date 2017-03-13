# Using try/except

try:
    import subprocess
    subprocess.check_checkoutput(['k'])
except Exception as ex:
    print "A %s exception happened because %s" % (type(ex).__name__, ex.args)
else:
    print "All Good"
