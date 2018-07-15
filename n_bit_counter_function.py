from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import numpy as np
import random
import string
import time
import math
import counter_adder as AND
import AES_function as aes

seed = input("請輸入seed : ")
random.seed(int(seed))

"""讀取compare出來的結果"""
compare_result = []
f = open('compare_result.txt', 'r')
line = f.readline()
while line :
	compare_result.append(line[0:-1])
	line = f.readline()
f.close()
#for i in range(10):
	#print(compare_result[i])

"""前面所產生的key"""
key_table = []
for i in range(len(compare_result)) :
	key_table_content = []
	for j in range(4) :
		key_table_content.append(''.join(random.choice(string.ascii_letters + string.digits) for x in range(14)) + "00")
	key_table.append(key_table_content)
#for i in range(10) :
	#print(key_table[i])

"""製作counter所需的key"""
counter_key = []
counter = []
for i in range(math.ceil(math.log(len(compare_result),2))+ 1) :
	counter_key_content = []
	for i in range(2):
		counter_key_content.append(''.join(random.choice(string.ascii_letters + string.digits) for x in range(14)) + "00")
	counter.append(counter_key_content[0])
	counter_key.append(counter_key_content)
#for i in range(math.ceil(math.log(len(compare_result),2))) :
	#print(counter_key[i])

"""計數器前置"""
first_bit_garbled = []#判斷是否compare數字為1
for i in range(len(compare_result)) :
	first_bit_garbled.append(AND.AND(counter_key[0],counter_key[0],counter_key[1],key_table[i][2:4]).get_encrypt_secret())
#for i in range(len(compare_result)) :
	#print(first_bit_garbled[i])
carry_bit_garbled = []#counter計算用
for i in range(math.ceil(math.log(len(compare_result),2))) :
	carry_bit_garbled.append(AND.AND(counter_key[i],counter_key[i],counter_key[i+1],counter_key[i]).get_encrypt_secret())
#for i in range(math.ceil(math.log(len(compare_result),2))) :
	#print(carry_bit_garbled[i])
"""counter start """
carry = ""
for i in range(len(compare_result)) :
	compare_key = aes.AESCrypto(compare_result[i])
	counter_bit_key = aes.AESCrypto(counter[0])
	for j in np.random.permutation(4) :
		try :
			if counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[i][j]))[-2:] == b'00' :
				carry = str(counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[i][j])))[2:18]
				#print("carry" + carry)
				counter[0] = str(counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[i][j])))[18:34]
				#print("counter" + counter[0])
		except :
			continue
	for j in range(1,math.ceil(math.log(len(compare_result),2))) :
		carry_key = aes.AESCrypto(carry)
		counter_bit_key = aes.AESCrypto(counter[j])
		for k in np.random.permutation(4) :
			try :
				if counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[j][k]))[-2:] == b'00' :
					carry = str(counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[j][k])))[2:18]
					counter[j] = str(counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[j][k])))[18:34]
			except :
				continue
	
for i in range(math.ceil(math.log(len(compare_result),2))) :
	print(counter[i])
f = open('counter_key.txt', 'w', encoding = 'UTF-8')
for i in range(len(counter_key)):
	f.write(str(counter_key[i]) + '\n')
f.close()
f = open('counter.txt', 'w', encoding = 'UTF-8')
for i in range(len(counter)):
	f.write(str(counter[i]) + '\n')
f.close()
