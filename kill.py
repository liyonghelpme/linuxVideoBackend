import os
f = open('spid')
pid = f.read()
f.close()
os.system('kill %s' % (pid))
