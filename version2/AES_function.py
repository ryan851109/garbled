from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

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
