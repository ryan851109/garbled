import os

name = input("請輸入名字 : ")
path = os.path.abspath('..') + '/' + name
if not os.path.isdir(path) :
	print('無此資料!!!')
	name = input("請再輸入一次 : ")
	path = os.path.abspath('..') + '/' + name

f = open(path + '/' + 'counter.txt', 'r')
result = []
line = f.readline()
while line:
	result.append(line[0:-1])
	line = f.readline()
f.close()
#print(result)
f = open(path + '/' + 'counter_key.txt', 'r')
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
number = ""
for i in range(len(result)) :
	if result[len(result) - 1 - i] == result_table[len(result_table) - 1 - i][0] :
		number = number + "0"
	else :
		number = number + "1"
print(int(number,2))
