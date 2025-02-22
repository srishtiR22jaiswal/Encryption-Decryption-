import base64
import os
from cryptography.fernet import Fernet

# Function to generate a key from user input
def get_key_from_password(password):
    key = base64.urlsafe_b64encode(password.ljust(32).encode()[:32])  # Ensure key length is 32 bytes
    return key

# Function to encrypt a message
def encrypt_message():
    password = input("\nEnter a secret key (this will be used for decryption too): ")
    key = get_key_from_password(password)
    cipher = Fernet(key)

    message = input("Enter the message you want to encrypt: ")
    encrypted_message = cipher.encrypt(message.encode())

    print("\nEncrypted Message:")
    print(encrypted_message.decode(), "\n")

    with open("encrypted_message.txt", "wb") as file:
        file.write(encrypted_message)
    print("The encrypted message has been saved in 'encrypted_message.txt'\n")

# Function to decrypt a message
def decrypt_message():
    password = input("\nEnter the secret key used for encryption: ")
    key = get_key_from_password(password)
    cipher = Fernet(key)

    try:
        with open("encrypted_message.txt", "rb") as file:
            encrypted_message = file.read()
    except FileNotFoundError:
        print("\nError: No encrypted message found! Please encrypt a message first.\n")
        return

    try:
        decrypted_message = cipher.decrypt(encrypted_message).decode()
        print("\nDecrypted Message:")
        print(decrypted_message, "\n")
    except Exception:
        print("\nError: Incorrect key or corrupted file! Decryption failed.\n")

# Menu-driven interface
def main():
    while True:
        print("========= Secure Message Encryption System =========")
        print("1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            encrypt_message()
        elif choice == "2":
            decrypt_message()
        elif choice == "3":
            print("\nExiting the program. Stay safe!\n")
            break
        else:
            print("\nInvalid choice! Please select a valid option (1-3).\n")

if __name__ == "__main__":
    main()
