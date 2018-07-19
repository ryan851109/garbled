from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np
import time
import AES_function as aes
import os

name = input("請輸入名字 : ")
path = os.path.abspath('..') + '/' + name
if not os.path.isdir(path) :
	print('無此資料!!!')
	name = input("請再輸入一次 : ")
	path = os.path.abspath('..') + '/' + name
garbled_table = []
fp = open(path + '/' + 'feature_garbled_table.txt', "r")
line = fp.readline()

while line:
	garbled_table.append(line[0:-1])
	line = fp.readline()
fp.close()
seed = input("請輸入seed : ")
search = input("請輸入想要的特徵 : ")
while len(search) > 1000 :
	print("過長的特徵!!!")
	search = input("請再次輸入想要的特徵 : ")
if len(search) < 1000 :
	search = ''.join('0' for x in range(1000-len(search))) + search
garbled_circuit = []
for i in range(len(garbled_table)) : 
	garbled_circuit_content = []
	garbled_circuit_content.append((garbled_table[i][3:35]).encode())
	garbled_circuit_content.append((garbled_table[i][40:72]).encode())
	garbled_circuit.append(garbled_circuit_content)
#for i in range(10) : 
	#print(garbled_circuit[i])
random.seed(int(seed))
key_table = []
for i in range(len(search)) :
	key_table_content = []
	for j in range(4) :
		key_table_content.append(''.join(random.choice(string.ascii_letters + string.digits) for x in range(14)) + "00")
	key_table.append(key_table_content)
#for i in range(10) : 
	#print(key_table[i])
search_key = []
compare_bit_start = time.time()
for i in range(len(search)) :
	if int(search[len(search) - i - 1]) == 0 :
		search_key.append(key_table[i][0])
	else :
		search_key.append(key_table[i][1])
#for i in range(10) :
	#print(search_key[i])
compare = []
for i in range(len(search)) :
	for j in np.random.permutation(2) :
		key = aes.AESCrypto(search_key[i])
		try :
			if key.decrypt(garbled_circuit[i][j])[-2:] == b'00' :
				compare.append(key.decrypt(garbled_circuit[i][j]))
		except :
			continue
compare_bit_end = time.time()
#for i in range(10) :
	#print(compare[i])
print("計算時間 : " + str(compare_bit_end - compare_bit_start))
f = open(path + '/' + 'compare_result.txt', 'w', encoding = 'UTF-8')
for i in range(len(compare)):
	f.write((compare[i]).decode() + '\n')
f.close()
