#module of 1bit full_adder by garbled circuit
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np

class AESCrypto():
	def __init__(self,key):
		self.key = key
		self.mode = AES.MODE_CBC
		#print(AES.block_size)

	def encrypt(self,text):
		if len(text)%16!=0:
			text=text+str((16-len(text)%16)*'0')
		cryptor = AES.new(self.key,self.mode,b'0000000000000000')
		self.ciphertext = cryptor.encrypt(text)
		return b2a_hex(self.ciphertext)

	def decrypt(self,text):
		cryptor = AES.new(self.key,self.mode,b'0000000000000000')
		plain_text  = cryptor.decrypt(a2b_hex(text))
		return plain_text.rstrip(b'\0')

class adder():
	def __init__(self,X,Y,CIN,SEED):
		self.X = X
		self.Y = Y
		self.CIN = CIN
		self.SEED = SEED
		key_table = ["","","","","","","","","","","","","","","",""]
		secret = ["0","1"]
		random.seed(int(self.SEED))
		for i in range(16):
			key_table[i] = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(14))
			key_table[i] = key_table[i] + "00"
		self.KEY_TABLE = key_table
		"""
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
		"""
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
		AxorBandCin_0 = AESCrypto(key_table[10])
		AxorBandCin_1 = AESCrypto(key_table[11])
		S_0 = AESCrypto(key_table[12])
		S_1 = AESCrypto(key_table[13])
		Cout_0 = AESCrypto(key_table[14])
		Cout_1 = AESCrypto(key_table[15])
		encrypt_secret_xor_1 = [B_0.encrypt(A_0.encrypt(AxorB_0.key)),                                                                 B_0.encrypt(A_1.encrypt(AxorB_1.key)),
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
		"""
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
		"""
		#print("請輸入A : ")
		key1 = AESCrypto(key_table[int(self.X)])
		#print("請輸入B : ")
		key2 = AESCrypto(key_table[int(self.Y) + 2])
		#print("請輸入C : ")
		key3 = AESCrypto(key_table[int(self.CIN) + 4])
		for i in np.random.permutation(4):
			try : 
				if key1.decrypt(key2.decrypt(encrypt_secret_xor_1[i]))[-2:] == b'00' :
					xor_1 =  AESCrypto(key1.decrypt(key2.decrypt(encrypt_secret_xor_1[i])))
			except : 
				continue
		for i in np.random.permutation(4):
			try : 
				if xor_1.decrypt(key3.decrypt(encrypt_secret_xor_2[i]))[-2:] == b'00' :
					self.SUM =  xor_1.decrypt(key3.decrypt(encrypt_secret_xor_2[i]))
					#print("Sum : " + str(Sum)[2:-1])
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
					self.COUT =  and_2.decrypt(and_1.decrypt(encrypt_secret_or[i]))
					#print("Cout : " + str(Cout)[2:-1])
			except :
				continue
	def get_sum(self):
		return self.SUM
	def get_cout(self):
		return str(self.COUT)
	def get_table(self):
		return self.KEY_TABLE
	def set_table(self,cin_0,cin_1):	
		self.KEY_TABLE[4] = cin_0
		self.KEY_TABLE[5] = cin_1	
