import os
os.system('pacmd list-sources > log')
f = open('log')
l = f.readlines()
count = 0
deviceName = None
for i in l:
    if count == 2 and i.find('name') != -1:
        res = i.replace(' ', '').replace('\n', '')
        res = res.split(':')
        res = res[1].replace('<', '').replace('>', '')
        deviceName = res
        break

    if i.find('index') != -1:
        count += 1
print deviceName

cmd = '(parec -d %s | oggenc -b 192 -o test.ogg --raw -)&' % (deviceName)
#cmd = '(parec -d %s | lame -r - test.mp3)&' % (deviceName)
print cmd
os.system(cmd)

npid1 = None
while True:
    os.system('ps aux | grep %s > pid' % (deviceName))
    pid = open('pid')
    l = pid.readlines()

    for i in l:
        if i.find('parec') != -1 and i.find('sh -c') == -1:
            npid1 = i
            break
    if npid1 != None:
        break

#npid1 = l[3]
#npid2 = l[1]

    
npid = npid1
npid = npid.split()[1]
print "record", npid
sp = open('spid', 'w')
sp.write(npid)
sp.close()
#import time
#time.sleep(20)

#print "kill", npid
#os.system('kill %s' % (npid))
