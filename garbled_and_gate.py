# garbled circuit with AND gate
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
	key_table = ["","","","","",""]
	secret = ["0","1"]
	for i in range(6):
		key_table[i] = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(14))
		key_table[i] = key_table[i] + "00"
	print("------------key table-----------")
	print(key_table[0])
	print(key_table[1])
	print(key_table[2])
	print(key_table[3])
	print(key_table[4])
	print(key_table[5])
	print("--------------------------------")
	X_0 = AESCrypto(key_table[0])
	X_1 = AESCrypto(key_table[1])
	Y_0 = AESCrypto(key_table[2])
	Y_1 = AESCrypto(key_table[3])
	Z_0 = AESCrypto(key_table[4])
	Z_1 = AESCrypto(key_table[5])
	encrypt_secret = [Y_0.encrypt(X_0.encrypt(Z_0.key)),
                          Y_0.encrypt(X_1.encrypt(Z_0.key)),
                          Y_1.encrypt(X_0.encrypt(Z_0.key)),
                          Y_1.encrypt(X_1.encrypt(Z_1.key))]
	print("------------encrypt_secret------")
	print(encrypt_secret[0])
	print(encrypt_secret[1])
	print(encrypt_secret[2])
	print(encrypt_secret[3])
	print("--------------------------------")
	print("請輸入X : ")
	key1 = AESCrypto(key_table[int(input())])
	print("請輸入Y : ")
	key2 = AESCrypto(key_table[int(input()) + 2])
	for i in np.random.permutation(4):
		try : 
			if key1.decrypt(key2.decrypt(encrypt_secret[i]))[-2:] == b'00' :
				print('output : ' +  str(key1.decrypt(key2.decrypt(encrypt_secret[i])))[2:-1])
				#print("secret succeed")
		except : 
			#print("secret fail")
			continue

if __name__ == "__main__":
	main()
