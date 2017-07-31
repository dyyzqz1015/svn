# -*- coding:utf-8 -*-

import csv

datafile='2.csv'
data=[]

with open (datafile,'rb') as f:
	f.readline()
	f.readline()
	cv=csv.reader(f)
	for line in cv:
		data.append(line)
