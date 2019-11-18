# Python based Encryption and Decryption

This is a hobby project written in Python and uses the **base64** library to encrypt or decrypt **all the folders in a given directory/path**. 
The encrypted files in a directory are unreadable (works best with images).

## Getting started:
- Create a test directory with some dummy files to run this script. **WARNING:** DO NOT RUN ```encrypt.py``` on your desktop. It will encrypt all files on your desktop which can crash your computer and make several files unreadable.  

- To encrypt content in the directory change the current directory to your test directory, type ```python encrypt.py``` and to decrypt the encrypted content in the same directory type ```python decrypt.py``` in your console. 
(Please note, ```decrypt.py``` will only help decrypt content already encrypted by ```encrypt.py```, if you run this script on unencrypted files they will be assumed to be encrypted files and ```decrypt.py``` will "decrypt" which will corrupt your files and no, ```encrypt.py``` will not encrypt ```decrypt.py```. Refer the code for more details.)

- Example:
```
$ mkdir test_directory
$ cd test_directory

fill your test_directory with test files 
and paste both encrypt.py and decrypt.py 
in the same directory and then run

$ python encrypt.py
$ python decrypt.py
```
