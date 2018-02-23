#!/usr/bin/env python
# _*_ coding:utf-8 _*_
file1 = "/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/1.txt"
file2 = "/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/2.txt"

f_diff = "/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/diff.txt"

# ---------- 对比文件内容，输出差异
f1 = open(file1, "r")
f2 = open(file2, "r")
file1 = f1.readlines()
file2 = f2.readlines()
f1.close()
f2.close()
print(len(file1))
outfile = open(f_diff, "w")
flag = 0
outfile.write("file1独有的数据：\n")
a = file1.index('sysname')
for i in file1:
	if i not in file2(b,len(file2)):
		outfile.write(i)
		flag = 1
outfile.write("file2独有的数据：\n")
b = file2.index("sysname")
for i in file2:
	if i not in file1(a,len(file1)):
		outfile.write(i)
		flag = 1
outfile.close()
if flag == 1:
	print("数据存在差异，请仔细核对！")