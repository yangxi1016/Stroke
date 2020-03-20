#!/usr/bin/python  
# coding = UFT-8
import os, sys
import re

result = []
output = sys.stdout
outputfile = open('Z-SYMPTOM-en-0204.txt', 'w', encoding='UTF-8')
sys.stdout = outputfile
f = open(r"DNorm-raw-a.txt", "r", encoding='UTF-8')
a = open(r"symmap.txt", "r", encoding='UTF-8')
lines = f.readlines()
lists = []
lines_a = a.readlines()
lists_a = []
for line in lines:
    lists.append(line.split())

for line_a in lines_a:
    lists_a.append(line_a.split())
# print len(lists),len(lists_a)
for j in range(0, 1026):
    for i in range(0, len(lists)):

        # outputfile.write (str(len(lists))+"\n")
        # outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"\n")
        if (len(lists[i]) >= 1):
            a = lists

            if (len(lists_a[j]) >= 1):
                c = ' '
                A = str(c.join(lists_a[2*j][0:len(lists_a[2*j])]))
                B = str(c.join(lists[i][1:len(lists[i])]) + ' ')
                nPos = B.find(A)
                k=(2*j)+1
                if nPos != -1:
                    outputfile.write(
                        str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                            lists[i][0]) + "\t" + str(nPos) + '\t' + str(
                            nPos + int(len(A))) + '\t' + str(
                            c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+'\n' + '\n')

            # if nPos != -1:
            # outputfile.write(str(lists[i][0])+'\t'+str(c.join(lists[i][1:len(lists[i])]))+'\n'+str(lists_a[j][1])+"\t"+str(nPos)+'\t'+str(nPos+int(len(lists_a[j][1])))+'\t'+str(c.join(lists_a[j][2:len(lists_a[j])]))+'\n'+'\n')
                n1Pos = B.find(A, nPos + int(len(lists_a[2*j][0])))
                if n1Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n1Pos) + '\t' + str(n1Pos + int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
                n2Pos = B.find(A, n1Pos + int(len(lists_a[2*j][0])))
                if n2Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n2Pos) + '\t' + str(n2Pos + int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
                n3Pos = B.find(A, n2Pos + int(len(lists_a[2*j][0])))
                if n3Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n3Pos) + '\t' + str(n3Pos + int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])])) + '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
                n4Pos = B.find(A, n3Pos + int(len(lists_a[2*j][0])))
                if n4Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n4Pos) + '\t' + str(n4Pos +int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
                n5Pos = B.find(A, n4Pos + int(len(lists_a[2*j][0])))
                if n5Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n5Pos) + '\t' + str(n5Pos + int(len(A)))+ '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
                n6Pos = B.find(A, n5Pos + int(len(lists_a[2*j][0])))
                if n6Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n6Pos) + '\t' + str(n6Pos + int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
                n7Pos = B.find(A, n6Pos + int(len(lists_a[2*j][0])))
                if n7Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n7Pos) + '\t' + str(n7Pos + int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])]))+ '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms" + '\n' + '\n')
                n8Pos = B.find(A, n7Pos + int(len(lists_a[2*j][0])))
                if n8Pos != -1:
                    outputfile.write(str(lists[i][0]) + '\t' + str(c.join(lists[i][1:len(lists[i])])) + '\n' + str(
                    lists[i][0]) + "\t" + str(n8Pos) + '\t' + str(n8Pos + int(len(A))) + '\t' + str(
                    c.join(lists_a[2*j][0:len(lists_a[2*j])])) + '\t'+ str(c.join(lists_a[k][0:len(lists_a[k])])) + '\t'+"Symptoms"+ '\n' + '\n')
outputfile.close()
sys.stdout = output
