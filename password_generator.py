import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

Master_Name= input("what is the master Name?")
print("Wellcome ", Master_Name, "!!!")

def write_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    try:
        with open("key.key", "rb") as file:
            SECRET_key = file.read()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1_200_000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(SECRET_key))
        return key
    except FileNotFoundError:
        print("Key file not found. A new key will be generated.")
        write_key()
        return load_key()

key = load_key()

fer = Fernet(key)

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            try:
                decrypted = fer.decrypt(passw.encode()).decode()
                print("user: ", user, "| Password :", decrypted)
            except Exception as e:
                print(f"user: {user} | Password : <decryption failed> ({type(e).__name__})")

def add():
    name= input("Enter the Account Name: ")
    Password= input("Enter the password: ")

    with open("password.txt","a") as f:
        f.write(name +"|"+ fer.encrypt(Password.encode()).decode() + "\n")

 
while True:
    mode= input("would you like to add a new password or view the current password (View/Add) or Q to quit")
    if mode == "q":
        break
    elif mode =="view":
        view()
    elif mode =="add":
        add()
    else:
        print("invaild mode")
        break
