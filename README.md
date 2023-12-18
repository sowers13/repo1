# repo1
Secure coding stuff

File_Encrypt_PBKDF2.py \n
// straightforward program that creates key with Password-Based Key Derivation Function 2. PBKDF2 is a stronger key derivation than a hash like sha256 because it makes brute force longer and uses a salt to prevent pre-computing a rainbow table of possible input offline and then quickly checking the output.
The file is encrypted using AES in CBC (cipher block-chaining) mode.
The file is decrypted by deriving a key using the password and salt


File_Transfer_Client.py
File_Transfer_Server.py
// File_Transfer_Server.py acts as a server for receiving encrypted files. It listens for incoming connections on the specified host and port and authenticates the client's username and password. Currently the only username and password is "user" and "password". If authentication is successful, the server expects the client to send an encrypted file and the received files are stored on the server-side with the name "received_from_[client_address].enc."

//File_Transfer_Client.py acts as the client for sending encrypted files to the server and will prompt you for the following:

Username: Enter your username.
Encryption Password: Enter the encryption password for securing the file.
Filename: Enter the name of the file you want to send.
The client encrypts the file if it's not already encrypted (using the same encryption method as File_Encrypt_PBKDF2.py).

File will be encrypted no matter what. In order for successful file transfer you will have to successfully authenticate to the server.

Important Notes:
Ensure that you have the necessary dependencies installed, including the "File_Encrypt_PBKDF2" module.
Make sure the server is running before attempting to send files from the client.
Replace the default server IP and port with your server's IP and port in File_Transfer_Client.py
update the user database for your real user accounts and passwords

