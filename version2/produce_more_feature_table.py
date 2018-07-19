import garbled_xor_gate_function as xor
import string
import random
import time
import os
"""
name = input("請輸入名字 : ")
path = os.path.abspath('..') + '/' + name
while os.path.isdir(path) :
	cover = input("已有此資料，是否覆蓋?(Y/N)")
	if cover == 'Y' :
		break
	elif cover == 'N' :
		name = input("請再輸入一次名字 : ")
		path = os.path.abspath('..') + '/' + name
	else :
		continue
if not os.path.isdir(path) :
	os.mkdir(path)
"""
file_content = []
file_name = input("檔案名稱 : ")
path = os.path.abspath('.') + '/' + file_name
try :
	f = open(path,'r')
	line = f.readline()
	while line :
		line = line.replace('\n','')
		#print(line)
		file_content.append(line)
		line = f .readline()
	f.close()
except :
	print("No file!!!")
	exit()

count = 0
f = open('feature_garbled_table.txt','r')
line = f.readline()
feature_length = len(line.split(','))
while line :
	count = count + 1
	line = f.readline()
f.close()

#times = int(input("請輸入你的資料數 : "))
times = len(file_content)
seed = input("請輸入您的seed : ")
random.seed(int(seed))
#f0 = open('seed.txt','w',encoding = 'UTF-8')
#f0.write(seed)
#f0.close()

for i in range(count) :
	a = xor.xor("0")
#print(str(count))
#print(str(feature_length))
#f1 = open(path + '/' + 'feature_garbled_table.txt', 'w', encoding = 'UTF-8')
f1 = open('feature_garbled_table.txt', 'a', encoding = 'UTF-8')
#f2 = open(path + '/' + 'key_table.txt', 'w', encoding = 'UTF-8')
f2 = open('key_table1.txt', 'w', encoding = 'UTF-8')
make_feature_garbled_table_time_start = time.time()
for file_count in range(times) :
	#feature = input("請輸入您的特徵 : ")
	feature = file_content[file_count]
	while len(feature) > (feature_length / 2) or len(feature) < 1: 
		print("第"+str(file_count+1)+"筆特徵長度錯誤!!!")
		exit()
		#feature = input("請再輸入一次您的特徵 : ")
	if len(feature) < (feature_length / 2) : 
		feature = ''.join('0' for x in range(int(feature_length / 2)-len(feature))) + feature
	feature_table = []
	for i in range(len(feature)) :
		feature_content = xor.xor(feature[len(feature)-i - 1])
		feature_table.append(feature_content)
	write_feature = []
	for i in range(len(feature_table)):
		write_feature.append(feature_table[i].get_encrypt_secret())
	f1.write(str(write_feature) + '\n')
	write_key = []
	for i in range(len(feature_table)):
		write_key.append(feature_table[i].get_key_table())
	f2.write(str(write_key) + '\n')
f1.close()
f2.close()
make_feature_garbled_table_time_end = time.time()
print("產生時間 : " + str(make_feature_garbled_table_time_end - make_feature_garbled_table_time_start))	
