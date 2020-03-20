#coding:utf-8  
import shutil  
readDir = "Chemical-Disease.txt"
writeDir = "Chemical-Disease-de.txt"
#txtDir = "/home/fuxueping/Desktop/１"  
lines_seen = set()  
outfile=open(writeDir,"w", encoding='UTF-8')
f = open(readDir,"r", encoding='UTF-8')
for line in f:  
    if line not in lines_seen:  
        outfile.write(line)  
        lines_seen.add(line)  
outfile.close()  
