#1bit full_adder by garbled circuit
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np

class AESCrypto():
	def __init__(self,key):
		self.key = key

	def encrypt(self,text):
		if len(text)%16!=0:
			text=text+str((16-len(text)%16)*'0')
		cryptor = AES.new(self.key,AES.MODE_CBC,b'0000000000000000')
		return b2a_hex(cryptor.encrypt(text))

	def decrypt(self,text):
		cryptor = AES.new(self.key,AES.MODE_CBC,b'0000000000000000')
		return (cryptor.decrypt(a2b_hex(text))).rstrip(b'\0')

def main():
	key_table = ["","","","","","","","","","","","","","","",""]
	secret = ["0","1"]
	#random.seed(1)  use the seed to control the random table
	for i in range(16):
		key_table[i] = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(14))
		key_table[i] = key_table[i] + "00"
	print("------------key table-----------")
	print(key_table[0])
	print(key_table[1])
	print(key_table[2])
	print(key_table[3])
	print(key_table[4])
	print(key_table[5])
	print(key_table[6])
	print(key_table[7])
	print(key_table[8])
	print(key_table[9])
	print(key_table[10])
	print(key_table[11])
	print(key_table[12])
	print(key_table[13])
	print(key_table[14])
	print(key_table[15])
	print("--------------------------------")
	A_0 = AESCrypto(key_table[0])
	A_1 = AESCrypto(key_table[1])
	B_0 = AESCrypto(key_table[2])
	B_1 = AESCrypto(key_table[3])
	Cin_0 = AESCrypto(key_table[4])
	Cin_1 = AESCrypto(key_table[5])
	AxorB_0 = AESCrypto(key_table[6])
	AxorB_1 = AESCrypto(key_table[7])
	AandB_0 = AESCrypto(key_table[8])
	AandB_1 = AESCrypto(key_table[9])
	S_0 = AESCrypto(key_table[10])
	S_1 = AESCrypto(key_table[11])
	AxorBandCin_0 = AESCrypto(key_table[12])
	AxorBandCin_1 = AESCrypto(key_table[13])
	Cout_0 = AESCrypto(key_table[14])
	Cout_1 = AESCrypto(key_table[15])
	encrypt_secret_xor_1 = [B_0.encrypt(A_0.encrypt(AxorB_0.key)),
                                B_0.encrypt(A_1.encrypt(AxorB_1.key)),
                                B_1.encrypt(A_0.encrypt(AxorB_1.key)),
                                B_1.encrypt(A_1.encrypt(AxorB_0.key))]
	encrypt_secret_xor_2 = [Cin_0.encrypt(AxorB_0.encrypt(S_0.key)),
                                Cin_0.encrypt(AxorB_1.encrypt(S_1.key)),
                                Cin_1.encrypt(AxorB_0.encrypt(S_1.key)),
                                Cin_1.encrypt(AxorB_1.encrypt(S_0.key))]
	encrypt_secret_and_1 = [B_0.encrypt(A_0.encrypt(AandB_0.key)),
                                B_0.encrypt(A_1.encrypt(AandB_0.key)),
                                B_1.encrypt(A_0.encrypt(AandB_0.key)),
                                B_1.encrypt(A_1.encrypt(AandB_1.key))]
	encrypt_secret_and_2 = [AxorB_0.encrypt(Cin_0.encrypt(AxorBandCin_0.key)),
                                AxorB_0.encrypt(Cin_1.encrypt(AxorBandCin_0.key)),
                                AxorB_1.encrypt(Cin_0.encrypt(AxorBandCin_0.key)),
                                AxorB_1.encrypt(Cin_1.encrypt(AxorBandCin_1.key))]
	encrypt_secret_or = [AandB_0.encrypt(AxorBandCin_0.encrypt(Cout_0.key)),
                             AandB_0.encrypt(AxorBandCin_1.encrypt(Cout_1.key)),
                             AandB_1.encrypt(AxorBandCin_0.encrypt(Cout_1.key)),
                             AandB_1.encrypt(AxorBandCin_1.encrypt(Cout_1.key))]
	print("------------encrypt_secret------")
	print(encrypt_secret_xor_1[0])
	print(encrypt_secret_xor_1[1])
	print(encrypt_secret_xor_1[2])
	print(encrypt_secret_xor_1[3])
	print(encrypt_secret_xor_2[0])
	print(encrypt_secret_xor_2[1])
	print(encrypt_secret_xor_2[2])
	print(encrypt_secret_xor_2[3])
	print(encrypt_secret_and_1[0])
	print(encrypt_secret_and_1[1])
	print(encrypt_secret_and_1[2])
	print(encrypt_secret_and_1[3])
	print(encrypt_secret_and_2[0])
	print(encrypt_secret_and_2[1])
	print(encrypt_secret_and_2[2])
	print(encrypt_secret_and_2[3])
	print(encrypt_secret_or[0])
	print(encrypt_secret_or[1])
	print(encrypt_secret_or[2])
	print(encrypt_secret_or[3])
	print("--------------------------------")
	print("請輸入A : ")
	key1 = AESCrypto(key_table[int(input())])
	print("請輸入B : ")
	key2 = AESCrypto(key_table[int(input()) + 2])
	print("請輸入C : ")
	key3 = AESCrypto(key_table[int(input()) + 4])
	for i in np.random.permutation(4):
		try : 
			if key1.decrypt(key2.decrypt(encrypt_secret_xor_1[i]))[-2:] == b'00' :
				xor_1 =  AESCrypto(key1.decrypt(key2.decrypt(encrypt_secret_xor_1[i])))
		except : 
			continue
	for i in np.random.permutation(4):
		try : 
			if xor_1.decrypt(key3.decrypt(encrypt_secret_xor_2[i]))[-2:] == b'00' :
				Sum =  xor_1.decrypt(key3.decrypt(encrypt_secret_xor_2[i]))
				print("Sum : " + str(Sum)[2:-1])
		except :
			continue
	###########################

	for i in np.random.permutation(4):
		try : 
			if key1.decrypt(key2.decrypt(encrypt_secret_and_1[i]))[-2:] == b'00' :
				and_1 =  AESCrypto(key1.decrypt(key2.decrypt(encrypt_secret_and_1[i])))
		except : 
			continue
	for i in np.random.permutation(4):
		try : 
			if key3.decrypt(xor_1.decrypt(encrypt_secret_and_2[i]))[-2:] == b'00' :
				and_2 =  AESCrypto(key3.decrypt(xor_1.decrypt(encrypt_secret_and_2[i])))
		except : 
			continue
	for i in np.random.permutation(4):
		try : 
			if and_2.decrypt(and_1.decrypt(encrypt_secret_or[i]))[-2:] == b'00' :
				Cout =  and_2.decrypt(and_1.decrypt(encrypt_secret_or[i]))
				print("Cout : " + str(Cout)[2:-1])
		except :
			continue
if __name__ == "__main__":
	main()
