from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random,string
import numpy as np
import AES_function as aes

class AND() :
	def __init__(self,COUNT_NOW,COUNT_NEXT,CARRY,CIN) :
		#print(COUNT_NOW)
		#print(COUNT_NEXT)
		#print(CARRY)
		#print(CIN)
		C_NOW_0 = aes.AESCrypto(COUNT_NOW[0])
		C_NOW_1 = aes.AESCrypto(COUNT_NOW[1])
		CARRY_0 = aes.AESCrypto(CARRY[0] + COUNT_NEXT[0])
		#print("KEY : " + CARRY_0.key)
		CARRY_1 = aes.AESCrypto(CARRY[1] + COUNT_NEXT[0])
		CARRY_2 = aes.AESCrypto(CARRY[0] + COUNT_NEXT[1])
		CIN_0 = aes.AESCrypto(CIN[0])
		CIN_1 = aes.AESCrypto(CIN[1])
		self.encrypt_secret = [CIN_1.encrypt(C_NOW_1.encrypt(CARRY_1.key)),
                                       CIN_0.encrypt(C_NOW_1.encrypt(CARRY_2.key)),
                                       CIN_1.encrypt(C_NOW_0.encrypt(CARRY_2.key)),
                                       CIN_0.encrypt(C_NOW_0.encrypt(CARRY_0.key))]
	def get_encrypt_secret(self) :
		return self.encrypt_secret
