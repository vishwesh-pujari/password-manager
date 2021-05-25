import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('KEY')
print(key)

fernet = Fernet(key)
message = "vishwesh"
encMessage = fernet.encrypt(message.encode())

decMessage = fernet.decrypt(encMessage).decode()

print(decMessage)
