import garbled_full_adder_1bit_function as garbled
import time

def main():
	list_bit = []
	print("請輸入seed : ")
	random_seed = input()
	seed = int(random_seed)
	print("請輸入第一個字串 : ")
	string_1 = input()
	while len(string_1) > 100000 :
		print("輸入過長，請重新輸入")
		string_1 = input()
	if len(string_1) < 100000 :
		string_1 = ''.join('0' for x in range(100000-len(string_1))) + string_1
	print("請輸入第二個字串 : ")
	string_2 = input()
	while len(string_2) > 100000 :
		print("輸入過長，請重新輸入")
		string_2 = input()
	if len(string_2) < 100000 :
		string_2 = ''.join('0' for x in range(100000-len(string_2))) + string_2
	carry = "0"
	tStart = time.time()#計時開始
	for i in range(100000):
		seed = seed * i
		bit = garbled.adder(string_1[99999-i],string_2[99999-i],carry,str(seed))
		list_bit.append(bit)
		if list_bit[i].get_cout()[2:18] == list_bit[i].get_table()[15]:
			carry = "1"
		else :
			carry = "0"
	tEnd = time.time()#計時結束
	print(tEnd - tStart)
	if list_bit[99999].get_cout()[2:18] == list_bit[99999].get_table()[15]:
		print("1")
	else :
		print("0") 
	#print(string_1)
	#print(string_2)
	#bit = garbled.adder('1','1','0')
	#print(bit.get_table())
	#print(bit.get_sum())
	#print(bit.get_cout())

if __name__ == "__main__":
	main()
