import csv
csvfile=file('/home/qz/svn/csvtest.csv','wb')
writer=csv.writer(csvfile)
writer.writerow(['id','url','key'])
data=[
	('1','python','org')
	('2','baidu','cn')
	('3','jd','com')
]
writer.writers(data)
csvfile.close()

