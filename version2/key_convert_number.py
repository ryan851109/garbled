import os
"""
name = input("請輸入名字 : ")
path = os.path.abspath('..') + '/' + name
if not os.path.isdir(path) :
	print('無此資料!!!')
	name = input("請再輸入一次 : ")
	path = os.path.abspath('..') + '/' + name
"""
#f = open(path + '/' + 'counter.txt', 'r')
try :
    f = open('counter.txt', 'r')
except :
    print("Wrong seed or can't finish privous action!!!")
    exit()
result = []
line = f.readline()
while line:
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.replace('\'','')
	line = line.replace('\n','')
	line = line.split(', ')	
	result.append(line)
	line = f.readline()
f.close()
#print(result)
#print(result[1])
#f = open(path + '/' + 'counter_key.txt', 'r')
f = open('counter_key.txt', 'r')
result_table = []
line = f.readline()
while line:
	result_table_content = []
	result_table_content.append(line[2:18])
	result_table_content.append(line[22:-3])
	result_table.append(result_table_content)
	line = f.readline()
f.close()
#print(result_table)
number = []
for i in range(len(result)) :
	number_content = ""
	for j in range(len(result[0])) :
		if result[i][len(result[0]) - 1 - j] == result_table[len(result_table) - 1 - j][0] :
			number_content = number_content + "0"
		else :
			number_content = number_content + "1"
	number.append(number_content)
	#print(number_content)
for i in range(len(number)) :
	print(int(number[i],2))
