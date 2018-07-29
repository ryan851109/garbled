from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

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
