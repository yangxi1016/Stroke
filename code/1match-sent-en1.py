#!/usr/bin/python  
# coding = UFT-8
import os, sys
import re

result = []
output = sys.stdout
outputfile = open('ctd-corpus.txt', 'w', encoding='UTF-8')
sys.stdout = outputfile
f = open(r"ctd-dis-chem-0.txt", "r", encoding='UTF-8')
a = open(r"Chemical-Disease-de.txt", "r", encoding='UTF-8')
lines = f.readlines()
lists = []
lines_a = a.readlines()
lists_a = []
for line in lines:
    lists.append(line.split("	"))

for line_a in lines_a:
    lists_a.append(line_a.split("	"))
# print len(lists),len(lists_a)
for j in range(0, len(lists_a) ):
     for i in range(0, len(lists) ):


        # outputfile.write (str(len(lists))+"\n")
        # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"\n")
        if  (int(lists[i][5]) == int(lists_a[j][5])):


            if ((lists[i][1]) == (lists_a[j][2])) & ((lists[i][3]) == (lists_a[j][0])):
                outputfile.write(
                    str(lists_a[j][4]) + "\t" + lists[i][0] + "\n")
            # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"###"+lists_a[j][3]+"###"+lists_a[j][3]+"###"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"%%%"+"\n")

# else:
# outputfile.write(str(lists[i])+"\n")
outputfile.close()
sys.stdout = output
