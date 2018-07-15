import garbled_xor_gate_function as xor
import string
import random
import time

seed = input("請輸入您的seed : ")
feature = input("請輸入您的特徵 : ")
random.seed(int(seed))
while len(feature) > 10 : 
	print("過長的特徵!!!")
	feature = input("請再輸入一次您的特徵 : ")
if len(feature) < 10 : 
	feature = ''.join('0' for x in range(10-len(feature))) + feature
feature_table = []
make_feature_garbled_table_time_start = time.time()
for i in range(len(feature)) :
	feature_content = xor.xor(feature[len(feature)-i - 1])
	feature_table.append(feature_content)
make_feature_garbled_table_time_end = time.time()
f = open('feature_garbled_table.txt', 'w', encoding = 'UTF-8')
for i in range(len(feature_table)):
	f.write(str(feature_table[i].get_encrypt_secret()) + '\n')
f.close()
f = open('key_table.txt', 'w', encoding = 'UTF-8')
for i in range(len(feature_table)):
	f.write(str(feature_table[i].get_key_table()) + '\n')
f.close()
print("產生時間 : " + str(make_feature_garbled_table_time_end - make_feature_garbled_table_time_start))

