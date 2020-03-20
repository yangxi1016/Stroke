#!/usr/bin/python  
# coding = UFT-8
import os, sys
import re

result = []
output = sys.stdout
outputfile = open('sen-dis-dru-bert.txt', 'w', encoding='UTF-8')
sys.stdout = outputfile
f = open(r"sen-dis-e1.txt", "r", encoding='UTF-8')
a = open(r"en-2.txt", "r", encoding='UTF-8')
lines = f.readlines()
lists = []
lines_a = a.readlines()
lists_a = []
for line in lines:
    lists.append(line.split())

for line_a in lines_a:
    lists_a.append(line_a.split())
# print len(lists),len(lists_a)
for i in range(0, len(lists) - 1):


        # outputfile.write (str(len(lists))+"\n")
        # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"\n")
        if (len(lists[i]) >= 5) & (len(lists_a[i]) >= 1) :


            #z = lists[i][4:len(lists[i])].insert(int(lists_a[j][1]) - int(lists[i][2]),"<e1>")

                c = ' <e2>'
                d = ' '
                e = ''
                f = ' </e2>'
                if (int(lists_a[i][1]) < int(lists[i][len(lists[i] )-2])):
                    y=d.join(lists[i][3:len(lists[i])-1])
                    z =list(y)
                    x=z.insert((int(lists_a[i][0]) ),c)
                    v = z.insert((int(lists_a[i][1])+1 ), c)
                    outputfile.write( str(e.join(z) ) +  "\n")

                    #outputfile.write(str(lists[i][0]) + "\t" + lists[i][1] + "\t" + lists[i][2] + "\t" + lists[i][3] + "\t" + str(e.join(z) ) +  "\n")
                if int(lists_a[i][0]) >int(lists[i][len(lists[i])-1]):
                    y = d.join(lists[i][3:len(lists[i] )-1])
                    z = list(y)
                    x = z.insert((int(lists_a[i][0]) +11 ), c)
                    v = z.insert((int(lists_a[i][1])+12), f)
                    outputfile.write( str(e.join(z)) + "\n")

                    #outputfile.write(str(lists[i][0]) + "\t" + lists[i][1] + "\t" + lists[i][2] + "\t" + lists[i][3] + "\t" + str(e.join(z)) + "\n")

            # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"###"+lists_a[j][3]+"###"+lists_a[j][3]+"###"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"%%%"+"\n")

# else:
# outputfile.write(str(lists[i])+"\n")
outputfile.close()
sys.stdout = output
