## This file will aid in encryption and base64 encoding using crypto and base 64 
from Crypto.Cipher import AES  # Import AES for encryption
from Crypto.Util.Padding import pad, unpad  # Import padding functions
from base64 import b64encode, b64decode  # Import base64 encoding and decoding
import os

#key creation:
key = 


# function to encrypt the message using cipher AES 
def encrypt_message(message):



# function to decrypt message using base64 and AES cipher
def decrypt_message(encrypted_message):
