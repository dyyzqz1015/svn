import os

# f1=cat svn.txt |paste -d ":" -s  

f=open('/home/qz/svn/svn') 
a=f.read() 
#print "no split:\n",a
b=a[1:-3]
c=b.split("::")

print "\tsvn","\tusername","\taccsee"
for i in range(0,len(c)):
	d=c[i].split(":")
	for j in range(1,len(d)):	
		print d[0]
		print d[1]
		print d[2]
#		svn=d[0]
#		username=d[j].split["="][0]
#		accsee=d[j].split["="][1]
#		print svn,username,accsee

f.close()

