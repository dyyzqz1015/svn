# -*- coding:utf-8 -*-

import os

# f1=cat svn.txt |paste -d ":" -s  

f=open('/home/qz/svn/svn') 
a=f.read() 
#print "no split:\n",a
b=a[1:-3]
c=b.split("::")

print "\tsvn","\tusername","\taccsee"

count=0
while count<len(c):
	

	d=c[count].split(":")
	for j in range(1,len(d)):	
#		print d[0],d[j].split("=")[0],d[j].split("=")[1]
		svn=d[0]
		username=d[j].split("=")[0]
		accsee=d[j].split("=")[1]
		print svn,username,accsee
	count=count+1
f.close()

