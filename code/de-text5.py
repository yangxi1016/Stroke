#!/usr/bin/python  
# coding = UFT-8
import os, sys
import re

result = []
output = sys.stdout
outputfile = open('stroke-0127-EN.txt', 'w', encoding='UTF-8')
sys.stdout = outputfile

a = open(r"stroke-0127.txt", "r", encoding='UTF-8')

lines_a = a.readlines()
lists_a = []


for line_a in lines_a:
    lists_a.append(line_a.split())
# print len(lists),len(lists_a)
for i in range(0, len(lists_a)):



            if (10>=len(lists_a[i])>= 5):
                c = ''
                d = ' '
                A =str(d.join(lists_a[i][3:len(lists_a[i])-1]))
                # d=str(c.join(lists[i][0:len(lists[i][0])]))+"\t"+str(c.join(lists[i][0:len(lists[i][1])]))+"\t"+str(c.join(lists[i][0:len(lists[i][2])]))

                outputfile.write(str(c.join(lists_a[i][0]))+"\t"+str(c.join(lists_a[i][1]))+"\t"+str(c.join(lists_a[i][2]))+"\t"+str(A)+"\t"+str(c.join(lists_a[i][len(lists_a[i])-1]))+"\t" "\n")
     # outputfile.write(str(lists[i][0])+'\t'+str(c.join(lists[i][1:len(lists[i])]))+'\n'+str(lists_a[j][0])+"\t"+str(n8Pos)+'\t'+str(n8Pos+int(lists_a[j][1]))+'\t'+str(c.join(lists_a[j][2:len(lists_a[j])]))+'\n'+'\n')
outputfile.close()
sys.stdout = output
