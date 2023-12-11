from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import os
import getpass

def encrypt(key, salt, filename):
    chunk_size = 64 * 1024
    output_file = filename + ".enc"
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = get_random_bytes(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(file_size.encode('utf-8'))
            outfile.write(IV)
            outfile.write(salt)  # Write the salt to the output file
            
            while True:
                chunk = infile.read(chunk_size)
                
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    print(f"File encrypted as {output_file}")

def decrypt(key, filename):
    chunk_size = 64 * 1024
    output_file = filename[:-4]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)
        salt = infile.read(16)  # Read the salt from the file

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)
    print(f"File decrypted as {output_file}")

def get_key(password, salt=None):
    if salt is None:
        salt = get_random_bytes(16)  # Generate a new salt
    key = PBKDF2(password, salt, dkLen=32, count=100000, hmac_hash_module=SHA256)
    return key, salt

def main():
    password = getpass.getpass("Enter encryption/decryption password: ")

    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")

    if choice == 'E':
        filename = input("Enter the filename to encrypt: ")
        key, salt = get_key(password)
        encrypt(key, salt, filename)
    elif choice == 'D':
        filename = input("Enter the filename to decrypt: ")
        # The salt is read from the file and then used to derive the key.
        key, _ = get_key(password)
        decrypt(key, filename)

if __name__ == "__main__":
    main()
