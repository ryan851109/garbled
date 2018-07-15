# garbled circuit with XOR gate
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np
import AES_function as aes

class xor():
	def __init__(self,INPUT_BIT):
		self.INPUT_BIT = INPUT_BIT
		self.key_table = ["","","",""]
		for i in range(4):
			self.key_table[i] = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(14))
			self.key_table[i] = self.key_table[i] + "00"
		Y_0 = aes.AESCrypto(self.key_table[0])
		Y_1 = aes.AESCrypto(self.key_table[1])
		Z_0 = aes.AESCrypto(self.key_table[2])
		Z_1 = aes.AESCrypto(self.key_table[3])
		if int(self.INPUT_BIT) == 0 :
			self.encrypt_secret = [Y_1.encrypt(Z_1.key),
                                          Y_0.encrypt(Z_0.key)]
		else :
			self.encrypt_secret = [Y_1.encrypt(Z_0.key),
                                          Y_0.encrypt(Z_1.key)]
	def get_key_table(self) :
		return self.key_table
	def get_encrypt_secret(self) : 
		return self.encrypt_secret	
