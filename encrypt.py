from cryptography.fernet import Fernet
import os

# File path of the text file you want to encrypt
file_path = "PATH/encrypter/EncryptFiles/test.txt"

# File path for where you want to save the encryption key
key_path = "PATH/encrypter/Keys/example.key"

# Generate a new key
key = Fernet.generate_key()

# Save the key to a file
with open(key_path, "wb") as key_file:
    key_file.write(key)

# Use the key to encrypt the text file
cipher = Fernet(key)
with open(file_path, "rb") as file:
    # Read the contents of the file
    file_data = file.read()
    # Encrypt the file data
    encrypted_data = cipher.encrypt(file_data)

# Save the encrypted data to the original file
with open(file_path, "wb") as file:
    file.write(encrypted_data)

print(f"{file_path} has been encrypted and saved, key saved at {key_path}")
