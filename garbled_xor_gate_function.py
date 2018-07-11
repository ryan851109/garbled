# garbled circuit with AND gate
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

class xor():
	def __init__(self,INPUT_BIT):
		self.INPUT_BIT = INPUT_BIT
		self.key_table = ["","","",""]
		for i in range(4):
			self.key_table[i] = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(14))
			self.key_table[i] = self.key_table[i] + "00"
		Y_0 = AESCrypto(self.key_table[0])
		Y_1 = AESCrypto(self.key_table[1])
		Z_0 = AESCrypto(self.key_table[2])
		Z_1 = AESCrypto(self.key_table[3])
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
