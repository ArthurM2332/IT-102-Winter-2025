

import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def generate_key():
    return os.urandom(16)

def encrypt(plaintext: str, key: bytes) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = cipher.update(padded_data) + cipher.finalize()
    return base64.b64encode(iv + ciphertext).decode()

def decrypt(encrypted_text: str, key: bytes) -> str:
    encrypted_data = base64.b64decode(encrypted_text)
    iv, ciphertext = encrypted_data[:16], encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    padded_plaintext = cipher.update(ciphertext) + cipher.finalize()
    return (unpadder.update(padded_plaintext) + unpadder.finalize()).decode()

key = generate_key()
print(f"Generated AES Key: {key}")
plaintext = input("Enter a plaintext message: ")
encrypted_message = encrypt(plaintext, key)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
