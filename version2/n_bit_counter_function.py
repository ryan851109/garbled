from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import numpy as np
import random
import string
import time
import math
import counter_adder as AND
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

"""讀取compare出來的結果"""
compare_result = []
#f = open(path + '/' + 'compare_result.txt', 'r')
f = open('compare_result.txt', 'r')
line = f.readline()
while line :
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.replace('\n','')
	line = line.replace('\'','')
	line = line.split(', ')
	every_compare_result = []
	for i in range(len(line)) :
		every_compare_result.append(line[i])
	compare_result.append(every_compare_result)
	line = f.readline()
f.close()
if compare_result[0][0] == "":
    try :
        os.remove(os.path.abspath('.') + "/counter.txt") 
        os.remove(os.path.abspath('.') + "/counter_key.txt")
    except :
        print("error seed")
        exit()
    print("error seed")
    exit()
#print(len(compare_result[0]))
#for i in range(10):
	#print(compare_result[i])

#seed = input("請輸入seed : ")
f =  open('seed.txt', 'r')
random.seed(int(f.readline()))

"""前面所產生的key"""
key_table = []
for i in range(len(compare_result)) :
	key_table_content = []
	for j in range(len(compare_result[0])) :
		every_key_table_content = []
		for k in range(4) :
			every_key_table_content.append(''.join(random.choice(string.ascii_letters + string.digits) for x in range(14)) + "00")
		key_table_content.append(every_key_table_content)
	key_table.append(key_table_content)
#print(key_table)

"""製作counter所需的key"""
make_counter_start = time.time()
counter_key = []
counter = []
for i in range(math.ceil(math.log(len(compare_result[0]),2))+ 1) :
	counter_key_content = []
	for i in range(2):
		counter_key_content.append(''.join(random.choice(string.ascii_letters + string.digits) for x in range(14)) + "00")
	counter.append(counter_key_content[0])
	counter_key.append(counter_key_content)
#for i in range(math.ceil(math.log(len(compare_result[0]),2))) :
	#print(counter_key[i])
#print("=================")
counter_result = []
for i in range(len(compare_result)) :
	"""計數器前置"""
	first_bit_garbled = []#判斷是否compare數字為1
	for j in range(len(compare_result[0])) :
		first_bit_garbled.append(AND.AND(counter_key[0],counter_key[0],counter_key[1],key_table[i][j][2:4]).get_encrypt_secret())
	#for i in range(len(compare_result)) :
		#print(first_bit_garbled[i])
	carry_bit_garbled = []#counter計算用
	for j in range(math.ceil(math.log(len(compare_result[0]),2))) :
		carry_bit_garbled.append(AND.AND(counter_key[j],counter_key[j],counter_key[j+1],counter_key[j]).get_encrypt_secret())
	#for i in range(math.ceil(math.log(len(compare_result),2))) :
		#print(carry_bit_garbled[i])
	"""counter start """
	carry = ""
	for j in range(len(compare_result[0])) :
		compare_key = aes.AESCrypto(compare_result[i][j])
		counter_bit_key = aes.AESCrypto(counter[0])
		for k in np.random.permutation(4) :
			try :
				if counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[j][k]))[-2:] == b'00' :
					carry = str(counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[j][k])))[2:18]
					#print("carry" + carry)
					counter[0] = str(counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[j][k])))[18:34]
					#print("counter" + counter[0])
			except :
				continue
		for k in range(1,math.ceil(math.log(len(compare_result[0]),2))) :
			carry_key = aes.AESCrypto(carry)
			counter_bit_key = aes.AESCrypto(counter[k])
			for l in np.random.permutation(4) :
				try :
					if counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[k][l]))[-2:] == b'00' :
						carry = str(counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[k][l])))[2:18]
						counter[k] = str(counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[k][l])))[18:34]
				except :
					continue
		counter[len(counter) - 1] = carry
	#print(counter)
	counter_result.append(counter)
	"""計數器歸零"""
	counter = []
	for j in range(math.ceil(math.log(len(compare_result[0]),2))+ 1) :
		counter.append(counter_key[j][0])
	#print(counter_result)
make_counter_end = time.time()
#for i in range(math.ceil(math.log(len(compare_result[0]),2))) :
#print(counter_result)
#f = open(path + '/' + 'counter_key.txt', 'w', encoding = 'UTF-8')
f = open('counter_key.txt', 'w', encoding = 'UTF-8')
for i in range(len(counter_key)):
	f.write(str(counter_key[i]) + '\n')
f.close()
#f = open(path + '/' + 'counter.txt', 'w', encoding = 'UTF-8')
f = open('counter.txt', 'w', encoding = 'UTF-8')
for i in range(len(counter_result)):
	f.write(str(counter_result[i]) + '\n')
f.close()
print("計算時間 : " + str(make_counter_end - make_counter_start))
