import os

def key_convert() :
	"""
	name = input("請輸入名字 : ")
	path = os.path.abspath('..') + '/' + name
	if not os.path.isdir(path) :
		print('無此資料!!!')
		name = input("請再輸入一次 : ")
		path = os.path.abspath('..') + '/' + name
	"""
	#f = open(path + '/' + 'counter.txt', 'r')
	f = open('counter.txt', 'r')
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
	for result_number in range(len(result)) :
		number_content = ""
		for result_position in range(len(result[0])) :
			if result[result_number][len(result[0]) - 1 - result_position] == result_table[len(result_table) - 1 - result_position][0] :
				number_content = number_content + "0"
			else :
				number_content = number_content + "1"
		number.append(number_content)
		#print(number_content)
	relative = []
	for number_position in range(len(number)) :
		#print(int(number[number_position],2))
		relative.append(int(number[number_position],2))
	#print("==========")

	min_relative = min(relative)
	index = []
	for relative_number in range(len(relative)) :
		if min_relative == relative[relative_number] :
			index.append(relative_number)

	file_content = []
	f = open(os.path.abspath('.') + '/information_data/information_data.txt','r')
	line = f.readline()
	while line :
		line = line.replace('\n','')
		file_content.append(line)
		line = f.readline()

	count = 1
	result = []
	for file_content_position in range(len(file_content)) :
		if file_content_position in index :
			#print(str(count) + '. ' + file_content[file_content_position])
			result.append(str(count) + '. ' + file_content[file_content_position])
			count = count + 1
	return result