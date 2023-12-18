import socket
import os
import getpass
from File_Encrypt_PBKDF2 import encrypt, get_key

#checks for previous file encryption
def encrypt_file_if_needed(password, filename):
    if not filename.endswith('.enc'):
        key, salt = get_key(password)
        encrypt(key, salt, filename)
        filename += ".enc"
    return filename

def send_file_to_server(server_ip, server_port, username, password, filename):
    encrypted_filename = encrypt_file_if_needed(password, filename)
     # create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    #Send username to the server for authentication check
    client_socket.send(username.encode())
    response = client_socket.recv(1024)
    if response != b"Username OK":
        print("Username not recognized. Goodbye.")
        client_socket.close()
        return

    #now send password for auth check
    client_socket.send(password.encode())
    response = client_socket.recv(1024)
    if response != b"Authenticated":
        print("Authentication failed. Goodbye.")
        client_socket.close()
        return

    # send encrypted file
    with open(encrypted_filename, 'rb') as f:
        client_socket.sendall(f.read())

    print(f"File {filename} sent successfully.")
    client_socket.close()

def main():
    server_ip = 'localhost'
    server_port = 12345
    username = input("Enter username: ")
    password = getpass.getpass("Enter encryption password: ")
    filename = input("Enter the filename to send: ")

    send_file_to_server(server_ip, server_port, username, password, filename)

if __name__ == "__main__":
    main()
