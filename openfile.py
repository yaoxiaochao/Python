#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
rootdir = '/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/配置备份0222'
list = os.listdir(rootdir)
for i in range(0,len(list)):
	path = os.path.join(rootdir,list[i])
	#print(list[i])
	file1 = path
	#print(path)
	rootdir2 = '/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/配置备份0228'
	path2 = os.path.join(rootdir2,list[i])
	file2 = path2
	#file2 = "/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/配置备份0228/"+list[i]
	f_diff = "/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/diff_.txt"
	f1 = open(file1, "r")
	f2 = open(file2, "r")
	file1 = f1.readlines()
	file2 = f2.readlines()
	f1.close()
	f2.close()
	outfile = open(f_diff, "a")
	flag = 0
	outfile.write(list[i]+"file1独有的数据：\n")
	for i in file1:
		if i not in file2:
			outfile.write(i)
			flag = 1
	outfile.write("file2独有的数据：\n")
	for i in file2:
		if i not in file1:
			outfile.write(i)
			flag = 1
	#outfile.close()
	if flag == 1:
		print("数据存在差异，请仔细核对！")
