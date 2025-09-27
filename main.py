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

        return encrypted_password
    

    def decryptPW(self, encrypted_password):
        # func to decrypt password imported from json 
        key = self.fetchKey()
        decrypted_password = key.decrypt(encrypted_password.decode())

        return decrypted_password
        


class PasswordCrud :
    

    def __init__(self): 
        
        print()




    def addPassword(self):
           
        #import json data
        with open("PW.json","r") as file:
            data = json.load(file)

        #take input for site to be added
        siteName = input("\n Enter site name :   ")

        #check if site already exists
        if siteName in data:
            print("\n WARNING - This site already exists   ")
        #else add the new site as outer key
        else:
            data[siteName] = {}
        
        #take input for username and password
        username = input("\n Enter username :   ")

        # here enrcrypt fn will be called
        password = input("\n Enter password :   ")

        #calling mngr class 
        objPasswordMngr = PasswordMngr(username)

        # calling encrypt fn 
        encrypted_value = objPasswordMngr.encryptPW(password)
        
        
        #updating password value with encrypted value
        data[siteName][username] = encrypted_value.decode()

        #write the new data to json
        with open("PW.json","w") as file:
            json.dump(data,file,indent=4)

        print("\n New username added !  ")





    def deletePassword(self):

        # load data from json 
        with open("PW.json","r") as file:
            data = json.load(file)
        
        # site name input
        sitename = input("\n Enter the sitename:    ")
       
        # choice for site deletion or user deletion
        option = input("\n A : to delete entire website\n B : to delete username only  \n\n")


        # site deletion
        if option == "A":
            if sitename in data :
                del data[sitename]
            else:
                print("\n WARNING - Site doest exist ")

        # user deletion
        else:
            username = input("\n Enter the username of which password will be DELETED :  ")

            if sitename in data and username in data[sitename]:
                del data[sitename][username]
            else:
                print("\n WARNING - Sitename or username doesnt exist   ")


        # dump data into json 
        with open("PW.json","w") as file:
             json.dump(data,file,indent=4)





    def showPassword(self):

        # taking site input
        sitename = input("\n Enter the site name :  ")

        # load json file to data
        with open("PW.json","r") as file:
            data = json.load(file)

        # take choice input
        choice = input(" \n Enter A to view all users of the site :\n Enter B to view password for a single user :  \n\n")
        

        # choice A : all users of a website
        if choice == "A":
            if sitename in data :
                print(data[sitename].keys())
            else:
                print("\n Site doesnt exist ")


        # choice B : single user password
        elif choice == "B" :
            username = input("\n Enter username of which password is to be displayed :  ")
            objPasswordMngr = PasswordMngr(username)
            password = data[sitename][username]
            password = password.encode()
            decodePass = objPasswordMngr.decryptPW(password)
            
            if sitename in data and username in data[sitename] :
                print("\n This is your password :",decodePass.decode())
            else:
                print("\n WARNING - showPassword : Site or User doesnt exist    ")


        # Incorrect choice warning
        else : 
            print(" \n WARNING - Enter correct choice ( ensure caps ) :   ")





    def updatePassword(self):
        
        # loading json file to data
        with open("Pw.json","r") as file:
            data = json.load(file)
       
        sitename = input("\n Enter name of the site :   ")

        if sitename in data :
            username = input("\n Enter the username :   ")

            # confirming old password with input
            if username in data[sitename] and sitename in data :
                oldPass = input("\n Enter old pasword :     ")
                actualOldPass = data[sitename][username]
                objPasswordMngr = PasswordMngr(username)
                enteredold = objPasswordMngr.decryptPW(actualOldPass.encode())

                # input and assign new password
                if oldPass.encode() == enteredold:
                    val = input("\n Enter new password :    ")
                    newPass = objPasswordMngr.encryptPW(val)
                    newPass = newPass.decode()
                    data[sitename][username] = newPass

                    print(" \n Password updated to :    ",val)

                    # dump data to json file 
                    with open("PW.json","w") as file:
                        json.dump(data,file,indent=4)

                # does not exist warnings
                else :
                    print("\n WARNING - Incorrect old password \n")
            else:
                print("\n WARNING - User doesnt exist in this site data \n")
        else:
            print("\n WARNING - Site doesnt exist in database \n")




def main():
    
    # Initiating Crud class
    objPasswordCrud = PasswordCrud()
    
    # Display menu
    print("\n 1. ADD new user and password \n 2. DISPLAY all site users / single user password \n 3. UPDATE existing user password \n 4. DELETE existing user password \n")
    
    # Input selected choice
    choice = input("\n Enter number respective to the task you want to perform :    ")

    # Call function using switch case
    command = choice

    match command:

        case "1":
            print("\n Your choice : ADD ")
            objPasswordCrud.addPassword()
        case "2":
            print("\n Your choice : DISPLAY ")
            objPasswordCrud.showPassword()
        case "3":
            print("\n Your choice : UPDATE ")
            objPasswordCrud.updatePassword()
        case "4":
            print("\n Your choice : DELETE ")
            objPasswordCrud.deletePassword()
        case _:
            print("\n WARNING - Incorrect input \n\n")


            
if __name__ == "__main__":
    main()





