import re
f1 = open('master.xml', 'r')
f2 = open('master-sample.xml','w')
for line in f1:
    f2.write(line.replace('&#4;' , ' '))
f1.close()
f2.close()
