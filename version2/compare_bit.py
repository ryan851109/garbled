from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np
import time
import AES_function as aes
import os
"""
name = input("請輸入名字 : ")
path = os.path.abspath('..') + '/' + name
if not os.path.isdir(path) :
	print('無此資料!!!')
	name = input("請再輸入一次 : ")
	path = os.path.abspath('..') + '/' + name
"""
garbled_table = []
#fp = open(path + '/' + 'feature_garbled_table.txt', "r")
fp = open('feature_garbled_table.txt', "r")
line = fp.readline()
#print(line)
#print(len(line))
while line :
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.replace('\n','')
	line = line.split(',')
	garbled_table_content = []
	every_garbled_table_content = []
	for i in range(len(line)) :
		if i % 2 == 0 :
			every_garbled_table_content.append((line[i][3:-1]).encode())
		else :
			every_garbled_table_content.append((line[i][3:-1]).encode())
			garbled_table_content.append(every_garbled_table_content)
			every_garbled_table_content = []
	garbled_table.append(garbled_table_content)
	line = fp.readline()
fp.close()
#print(len(garbled_table))
#seed = input("請輸入seed : ")
fp = open('seed.txt', "r")
random.seed(int(fp.readline()))
search = input("請輸入想要的特徵 : ")
while len(search) > len(garbled_table[0]) :
	print("過長的特徵!!!")
	search = input("請再次輸入想要的特徵 : ")
if len(search) < len(garbled_table[0]) :
	search = ''.join('0' for x in range(len(garbled_table[0])-len(search))) + search

compare_bit_start = time.time()

key_table = []
for i in range(len(garbled_table)) :
	key_table_content = []
	for j in range(len(search)) :
		every_key_table_content = []
		for k in range(4) :
			every_key_table_content.append(''.join(random.choice(string.ascii_letters + string.digits) for x in range(14)) + "00")
		key_table_content.append(every_key_table_content)
	key_table.append(key_table_content)
#print(key_table)

write_compare = []
"""開始計算差異"""
for i in range(len(garbled_table)) :
	search_key = []
	for j in range(len(search)) :
		if int(search[len(search) - i - 1]) == 0 :
			search_key.append(key_table[i][j][0])
		else :
			search_key.append(key_table[i][j][1])
	#for i in range(10) :
		#print(search_key[i])
	compare = []
	for j in range(len(search)) :
		key = aes.AESCrypto(search_key[j])
		for k in np.random.permutation(2) :
			try :
				if key.decrypt(garbled_table[i][j][k])[-2:] == b'00' :
					compare.append((key.decrypt(garbled_table[i][j][k])).decode())
			except :
				continue
	#print(compare)
	write_compare.append(compare)
compare_bit_end = time.time()
#for i in range(10) :
	#print(compare[i])
print("計算時間 : " + str(compare_bit_end - compare_bit_start))
#f = open(path + '/' + 'compare_result.txt', 'w', encoding = 'UTF-8')
f = open('compare_result.txt', 'w', encoding = 'UTF-8')
for i in range(len(write_compare)):
	f.write(str(write_compare[i]) + '\n')
f.close()
#print(write_compare)
