## This file will aid in encryption and base64 encoding using crypto and base 64 
from Crypto.Cipher import AES  # Import AES for encryption
from Crypto.Util.Padding import pad, unpad  # Import padding functions
from base64 import b64encode, b64decode  # Import base64 encoding and decoding
import os

#key creation:
key = os.urandom(32)


# function to encrypt the message using cipher AES 
def encrypt_message(message):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    return b64encode(iv + encrypted).decode()


# function to decrypt message using base64 and AES cipher
def decrypt_message(encrypted_message):
    encrypted_message = b64decode(encrypted_message)
    iv = encrypted_message[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_message[16:]), AES.block_size)
    return decrypted.decode()
