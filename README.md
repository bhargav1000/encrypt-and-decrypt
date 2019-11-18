# Python based Encryption and Decryption

This is a hobby project written in Python and uses the **base64** library to encrypt or decrypt **all the folders in a given directory/path**. 
The encrypted files in a directory are unreadable (works best with images).

## Getting started:
- Create a test directory to run this script. 
**WARNING:** DO NOT RUN ```encrypt.py``` on your desktop. It will encrypt all files on your desktop which can cause your computer to crash and make several files unreadable.  

- To encrypt content in the directory, type ```python encrypt.py``` and to decrypt the encrypted content type ```python decrypt.py``` in your console. 
(Please note, ```decrypt.py``` will only help decrypt content already encrypted by ```encrypt.py```, if you run this script on unencrypted files they will be assumed to be encrypted files and ```decrypt.py``` will "decrypt" which will corrupt your files and no, ```encrypt.py``` will not encrypt ```decrypt.py```. Refer the code for more details.) 
