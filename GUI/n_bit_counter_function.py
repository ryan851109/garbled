from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import numpy as np
import random
import string
#import time
import math
import counter_adder_function as AND
import AES_function as aes
import os

def counter(seed) :
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
		for line_position in range(len(line)) :
			every_compare_result.append(line[line_position])
		compare_result.append(every_compare_result)
		line = f.readline()
	f.close()
	#print(len(compare_result))
	#print(len(compare_result[0]))

	#seed = input("請輸入seed : ")
	#f =  open('seed.txt', 'r')
	#random.seed(int(f.readline()))
	random.seed(int(seed))

	"""前面所產生的key"""
	key_table = []
	for file_number in range(len(compare_result)) :
		key_table_content = []
		for compare_length in range(len(compare_result[0])) :
			every_key_table_content = []
			for key_number in range(4) :
				every_key_table_content.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14)) + "00")
			key_table_content.append(every_key_table_content)
		key_table.append(key_table_content)
	#print(len(key_table[0]))

	"""製作counter所需的key"""
	#make_counter_start = time.time()
	counter_key = []
	counter = []
	for counter_length in range(math.ceil(math.log(len(compare_result[0]),2))+ 1) :
		counter_key_content = []
		for key_position in range(2):
			counter_key_content.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14)) + "00")
		counter.append(counter_key_content[0])
		counter_key.append(counter_key_content)
	#for i in range(math.ceil(math.log(len(compare_result[0]),2))) :
		#print(counter_key[i])
	#print("=================")
	counter_result = []
	for file_number in range(len(compare_result)) :
		"""計數器前置"""
		first_bit_garbled = []#判斷是否compare數字為1
		for compare_length in range(len(compare_result[0])) :
			first_bit_garbled.append(AND.AND(counter_key[0],counter_key[0],counter_key[1],key_table[file_number][compare_length][2:4]).get_encrypt_secret())
		#for j in range(len(compare_result[0])) :
			#print(first_bit_garbled[j])
		carry_bit_garbled = []#counter計算用
		for counter_length in range(math.ceil(math.log(len(compare_result[0]),2))) :
			carry_bit_garbled.append(AND.AND(counter_key[counter_length],counter_key[counter_length],counter_key[counter_length+1],counter_key[counter_length]).get_encrypt_secret())
		#for i in range(math.ceil(math.log(len(compare_result),2))) :
			#print(carry_bit_garbled[i])
		"""counter start """
		carry = ""
		for compare_length in range(len(compare_result[0])) :
			compare_key = aes.AESCrypto(compare_result[file_number][compare_length])
			#print(compare_result[i][j])
			counter_bit_key = aes.AESCrypto(counter[0])
			for random_decrypt_first in np.random.permutation(4) :
				try :
					if counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[compare_length][random_decrypt_first]))[-2:] == b'00' :
						carry = str(counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[compare_length][random_decrypt_first])))[2:18]
						#print("carry" + carry)
						counter[0] = str(counter_bit_key.decrypt(compare_key.decrypt(first_bit_garbled[compare_length][random_decrypt_first])))[18:34]
						#print("counter" + counter[0])
				except :
					continue
			for counter_position in range(1,math.ceil(math.log(len(compare_result[0]),2))) :
				carry_key = aes.AESCrypto(carry)
				counter_bit_key = aes.AESCrypto(counter[counter_position])
				for random_decrypt_counter in np.random.permutation(4) :
					try :
						if counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[counter_position][random_decrypt_counter]))[-2:] == b'00' :
							carry = str(counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[counter_position][random_decrypt_counter])))[2:18]
							counter[counter_position] = str(counter_bit_key.decrypt(carry_key.decrypt(carry_bit_garbled[counter_position][random_decrypt_counter])))[18:34]
					except :
						continue
			counter[len(counter) - 1] = carry
		#print(counter)
		counter_result.append(counter)
		"""計數器歸零"""
		counter = []
		for counter_position in range(math.ceil(math.log(len(compare_result[0]),2))+ 1) :
			counter.append(counter_key[counter_position][0])
		#print(counter_result)
	#make_counter_end = time.time()
	#for i in range(math.ceil(math.log(len(compare_result[0]),2))) :
	#print(counter_result)
	#f = open(path + '/' + 'counter_key.txt', 'w', encoding = 'UTF-8')
	f = open('counter_key.txt', 'w', encoding = 'UTF-8')
	for counter_key_position in range(len(counter_key)):
		f.write(str(counter_key[counter_key_position]) + '\n')
	f.close()
	#f = open(path + '/' + 'counter.txt', 'w', encoding = 'UTF-8')
	f = open('counter.txt', 'w', encoding = 'UTF-8')
	for counter_result_position in range(len(counter_result)):
		f.write(str(counter_result[counter_result_position]) + '\n')
	f.close()
	#print("計算時間 : " + str(make_counter_end - make_counter_start))