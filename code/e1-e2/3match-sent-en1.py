#!/usr/bin/python  
# coding = UFT-8
import os, sys
import re

result = []
output = sys.stdout
outputfile = open('sen-dis-e1.txt', 'w', encoding='UTF-8')
sys.stdout = outputfile
f = open(r"sen-dis-drugs-A1.txt", "r", encoding='UTF-8')
a = open(r"en-1.txt", "r", encoding='UTF-8')
lines = f.readlines()
lists = []
lines_a = a.readlines()
lists_a = []
for line in lines:
    lists.append(line.split())

for line_a in lines_a:
    lists_a.append(line_a.split())
# print len(lists),len(lists_a)
for i in range(0, len(lists) ):


        # outputfile.write (str(len(lists))+"\n")
        # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"\n")
        if (len(lists[i]) >= 5) & (len(lists_a[i]) >= 1) :
            #n = int(lists[i][3])
            c=' <e1>'
            d=' '
            e=''
            f=' </e1>'
            #z = lists[i][4:len(lists[i])].insert(int(lists_a[j][1]) - int(lists[i][2]),"<e1>")
            y=d.join(lists[i][3:len(lists[i])])
            #y=re.findall(r"(.+?)###Chemical###", X)
            z =list(y)
            x=z.insert((int(lists_a[i][0])-1),c)
            v = z.insert((int(lists_a[i][1]) +1), f)
            #if (int(lists[i][2]) <= int(lists_a[j][2])) & (int(lists[i][3]) >= int(lists_a[j][3])):
            outputfile.write(str(lists[i][0]) + "\t" + lists[i][1] + "\t" + lists[i][2] + "\t"  + str(e.join(z) ) + "\t" + lists_a[i][0] + "\t" + lists_a[i][1] + "\n")
            # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"###"+lists_a[j][3]+"###"+lists_a[j][3]+"###"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"%%%"+"\n")

# else:
# outputfile.write(str(lists[i])+"\n")
outputfile.close()
sys.stdout = output
