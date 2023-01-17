from cryptography.fernet import Fernet
import os

# File path of the text file you want to decrypt
file_path = "PATH/encrypter/EncryptFiles/test.txt"

# File path for the key file
key_path = "PATH/encrypter/Keys/example.key"

# Open the key file
with open(key_path, "rb") as key_file:
    key = key_file.read()

# Use the key to decrypt the text file
cipher = Fernet(key)
with open(file_path, "rb") as file:
    # Read the contents of the file
    encrypted_data = file.read()
    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted data to the original file
with open(file_path, "wb") as file:
    file.write(decrypted_data)

print(f"{file_path} has been decrypted and saved")
