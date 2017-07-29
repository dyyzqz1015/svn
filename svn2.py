a="[/svn1]:user1=rw:user2=rw:user3=r:user4=no"
b=a.split(":")
c=b[1:]
d=c[0].split("=")

list1=[b[0],d[0],d[1],d[1],d[1]]
print "\tlist:\n",list1
print "\tsvn","\tuser","\tw","\tr","\tn"
j=0
for i in range(0,len(c)):
	rep=b[j]
	username=c[i].split("=")[0]

	write=c[i].split("=")[1]
#	read=c[i].split("=")[1]
	print rep,username,write

#	no=c[i].split("=")[1]
 #   print rep,username,write,read
#	list=[b[j],c[i].split("=")[0]]
    
#	print list




#print "list:\n",list
#print "b:\n",b
#print "c:\n",c
#print "d:\n",d
#print "\tsvn","\tuser","\tw","\tr","\tn"
#for i in range(0,len(c)):
#
#	print '\t',b[0],c[i].split("=")[0],'\n'
