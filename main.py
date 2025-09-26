import json
from cryptography.fernet import Fernet


class PasswordMngr :

    def __init__(self, username):
        self.username = username



    def fetchKey(self):
        # func to get encryption/ decryption key from txt file
        with open("key.txt","r") as file:
            key = file.read()
            
        f = Fernet(key)
        return f


    def encryptPW(self,password):
        # func to encrypt entered password for saving in json
        key = self.fetchKey()
        encrypted_password = key.encrypt(password.encode()) 

        print(f"Encrypted Password: {encrypted_password }")
        return encrypted_password
    
    def decryptPW(self, encrypted_password):
        # func to decrypt password imported from json 
        key = self.fetchKey()
        decrypted_password = key.decrypt(encrypted_password.decode())

        print("decrypt pw:",decrypted_password)
        return decrypted_password
        


class PasswordCrud :
    

    def __init__(self): 
        
        print("init func for class PasswordCrud")


    def addPassword(self):
        # func to add a new user and respective password
        print() 
    

    def deletePassword(self):
        # func to delete existing password 
        print()

    def showPassword(self):
        # func to show all users of site o password of specific user
        print()


def main():
    print("Hello from the main function!")
    

if __name__ == "__main__":
    main()





