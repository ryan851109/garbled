from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np
import AES_function as aes

class AND():
	def __init__(self,COUNT_NOW,COUNT_NEXT,SET_KEY):
		C_NOW_0 = aes.AESCrypto(COUNT_NOW[0])
		C_NOW_1 = aes.AESCrypto(COUNT_NOW[1])
		C_NEXT_0 = aes.AESCrypto(COUNT_NEXT[0])
		C_NEXT_1 = aes.AESCrypto(COUNT_NEXT[1])
		Z_0 = aes.AESCrypto(SET_KEY[0])
		Z_1 = aes.AESCrypto(SET_KEY[1])
		self.encrypt_secret = [Z_1.encrypt(C_NOW_1.encrypt(C_NEXT_1.key)),
                                       Z_0.encrypt(C_NOW_1.encrypt(C_NEXT_0.key)),
                                       Z_1.encrypt(C_NOW_0.encrypt(C_NEXT_0.key)),
                                       Z_0.encrypt(C_NOW_0.encrypt(C_NEXT_0.key))]
	def get_encrypt_secret(self) :
		return self.encrypt_secret
