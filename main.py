import json
from cryptography.fernet import Fernet


class PasswordMngr :

    def __init__(self, username):
        self.username = username



    def fetchKey(self):
        # func to get encryption/ decryption key from txt file
        print()


    def encryptPW(self,password):
        # func to encrypt entered password for saving in json
        print()
    
    def decryptPW(self, encrypted_password):
        # func to decrypt password imported from json 
        print()
        


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





