# repo1
Secure coding stuff

File_Encrypt_PBKDF2.py \n
// straightforward program that creates key with Password-Based Key Derivation Function 2. PBKDF2 is a stronger key derivation than say a hash like sha256 because it makes brute force longer and uses a salt to prevent pre-computing a rainbow table of possible input offline and then quickly checking the output.
// The file is encrypted using AES in CBC (cipher block-chaining) mode.
// The file is decrypted by deriving a key using the password and salt
