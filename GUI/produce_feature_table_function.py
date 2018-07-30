import garbled_xor_gate_function as xor
import string
import random
#import time
import os
from tkinter import messagebox

def produce(file_name,seed):
	new_file = True 
	path = os.path.abspath('.') + '/' + "information_data" 
	while os.path.exists(path + '/information_data.txt') :
		if messagebox.askokcancel("Cover", "已有資料是否覆蓋?") :
			new_file = True
			break
		if messagebox.askokcancel("New", "是否新增資料?") :
			new_file = False
			break
		if messagebox.askokcancel("New", "是否取消動作?") :
			return ("動作已取消",True)
		"""
		cover = input("已有資料，請選擇要執行動作 : (新增(N)/覆蓋(O)/取消(C))")
		if cover == 'O' :
			new_file = True
			break
		elif cover == 'N' :
			new_file = False
			break
		elif cover == 'C' :
			exit()
		else :
			continue
		"""
	if not os.path.isdir(path) :
		os.mkdir(path)

	if not new_file :
		information_data = open(path + '/' + 'information_data.txt','a',encoding = 'UTF-8')
	else :
		information_data = open(path + '/' + 'information_data.txt','w',encoding = 'UTF-8')

	file_content = []
	#file_name = input("檔案名稱 : ")
	path = os.path.abspath('.') + '/feature.txt'
	try :
		f = open(path,'r')
		line = f.readline()
		while line :
			line = line.replace('\n','')
			#print(line)
			file_content.append(line)
			line = f .readline()
	except :
		information_data.close()
		f.close()
		#print("No file!!!")
		return ("檔案錯誤",True)
		exit()
		
	f.close()

	if not new_file :
		count = 0
		f = open('feature_garbled_table.txt','r')
		line = f.readline()
		feature_length = len(line.split(', '))
		while line :
			count = count + 1
			line = f.readline()
		f.close()
	else :
		feature_length = 0

	#times = int(input("請輸入你的資料數 : "))
	times = len(file_content)
	#seed = input("請輸入您的seed : ")
	random.seed(int(seed))
	f0 = open('seed.txt','w',encoding = 'UTF-8')
	f0.write(seed)
	f0.close()
	if not new_file :
		for had_feature_number in range(int(count*feature_length / 2)) :
			xor.xor("0")
	#f1 = open(path + '/' + 'feature_garbled_table.txt', 'w', encoding = 'UTF-8')
	if not new_file :
		f1 = open('feature_garbled_table.txt', 'a', encoding = 'UTF-8')
	else :
		f1 = open('feature_garbled_table.txt', 'w', encoding = 'UTF-8')
	#f2 = open(path + '/' + 'key_table.txt', 'w', encoding = 'UTF-8')
	#f2 = open('key_table.txt', 'w', encoding = 'UTF-8')
	#make_feature_garbled_table_time_start = time.time()
	for file_count in range(times) :
		#feature = input("請輸入您的特徵 : ")
		feature = file_content[file_count]
		if not new_file :
			if (len(feature) > (feature_length / 2)) or len(feature) < 1 : 
				#print("第"+str(file_count+1)+"筆特徵長度錯誤!!!")
				#exit()
				return ("第"+str(file_count+1)+"筆特徵長度錯誤!!!",False)
				#feature = input("請再輸入一次您的特徵 : ")
			if len(feature) < (feature_length / 2) : 
				feature = ''.join('0' for _ in range(int(feature_length / 2)-len(feature))) + feature
		else :
			if (len(feature) > feature_length and file_count != 0) or len(feature) < 1: 
				return ("第"+str(file_count+1)+"筆特徵長度錯誤!!!",False)
				#print("第"+str(file_count+1)+"筆特徵長度錯誤!!!")
				#exit()
				#feature = input("請再輸入一次您的特徵 : ")
			if file_count == 0 :
				feature_length = len(feature)
			if len(feature) < feature_length :
				feature = ''.join('0' for _ in range(feature_length-len(feature))) + feature
		feature_table = []
		for new_feature_position in range(len(feature)) :
			feature_content = xor.xor(feature[len(feature)- new_feature_position - 1])
			feature_table.append(feature_content)
		#print(feature)
		write_feature = []
		for feature_table_position in range(len(feature_table)):
			write_feature.append(feature_table[feature_table_position].get_encrypt_secret())
		f1.write(str(write_feature) + '\n')
		#write_key = []
		#for i in range(len(feature_table)):
			#write_key.append(feature_table[i].get_key_table())
			#print(feature_table[i].get_key_table())
		#f2.write(str(write_key) + '\n')
	f1.close()
	#f2.close()
	#make_feature_garbled_table_time_end = time.time()
	
	f = open(file_name,'r')
	line = f.readline()
	while line :
		information_data.write(line)
		line = f .readline()
	f.close()
	information_data.close()
	
	#print("產生時間 : " + str(make_feature_garbled_table_time_end - make_feature_garbled_table_time_start))
	return ("轉換成功",True)