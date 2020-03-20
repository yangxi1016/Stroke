#!/usr/bin/python  
# coding = UFT-8
import os, sys
import re

result = []
output = sys.stdout
outputfile = open('ing-0127-f-EN.txt', 'w', encoding='UTF-8')
sys.stdout = outputfile

a = open(r"ing-0127-f.txt", "r", encoding='UTF-8')

lines_a = a.readlines()
lists_a = []


for line_a in lines_a:
    lists_a.append(line_a.split())
# print len(lists),len(lists_a)
for i in range(0, len(lists_a)):
     if (len(lists_a[i])>= 1):


            if ('|t|' not in lists_a[i][0])&('|a|' not in lists_a[i][0]):
                c = ''
                d = ' '
                A =str(d.join(lists_a[i][3:len(lists_a[i])-2]))
                # d=str(c.join(lists[i][0:len(lists[i][0])]))+"\t"+str(c.join(lists[i][0:len(lists[i][1])]))+"\t"+str(c.join(lists[i][0:len(lists[i][2])]))

                outputfile.write(str(c.join(lists_a[i][0]))+"\t"+str(c.join(lists_a[i][1]))+"\t"+str(c.join(lists_a[i][2]))+"\t"+str(A)+"\t"+str(c.join(lists_a[i][len(lists_a[i])-2]))+"\t"+str(c.join(lists_a[i][len(lists_a[i])-1]))+"\t" "\n")
     # outputfile.write(str(lists[i][0])+'\t'+str(c.join(lists[i][1:len(lists[i])]))+'\n'+str(lists_a[j][0])+"\t"+str(n8Pos)+'\t'+str(n8Pos+int(lists_a[j][1]))+'\t'+str(c.join(lists_a[j][2:len(lists_a[j])]))+'\n'+'\n')
outputfile.close()
sys.stdout = output
