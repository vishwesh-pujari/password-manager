# password-manager
Password Manager GUI application created using PyQt5 GUI library and Sqlite Database in Python3

To run the applications first install some dependencies
1. pip3 install PyQt5
2. pip3 install cryptography
3. pip install python-dotenv

Then run the application as:
python3 passwordManager.py

### Securing-Passwords

For encrypting passwords, fernet module of the cryptography package has been used.

.env file is used to store the KEY which will be used to encrypt and decrypt passwords

.env file is generally used to store such sensitive information in key-value pair format

python-dotenv package is used to interface such .env files
