import socket
import threading
import os

# mock user data
users = {
    "user": "password"
}

#function to handle each connected client
def handle_client(client_socket, client_addr):
    username = client_socket.recv(1024).decode()
    if username not in users:
        client_socket.send(b"File failed to send. Username not recognized")
        client_socket.close()
        return
    else:
        client_socket.send(b"Username OK")

    password = client_socket.recv(1024).decode()
    if password == users[username]:
        client_socket.send(b"Authenticated")
    else:
        client_socket.send(b"Authentication failed")
        client_socket.close()
        return

    #receive encrypted file and store it locally
    with open(f"received_from_{client_addr}.enc", 'wb') as f:
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            f.write(data)

    print(f"Encrypted file received and stored from {username}")
    client_socket.close()

#listen for incoming connections
def start_server(host='localhost', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server started, waiting for connections...")

    #accept incoming client connections and handle them in separate threads
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr[0])).start()

if __name__ == "__main__":
    start_server()
