from cryptography.fernet import Fernet #enable us encrypt text

"""
#uncomment function to generate encryption key then write to key.key file
#comment after finishing
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()
"""
#get the encryption key
def load_key():
    file = open("password_manager/key.key","rb")
    key = file.read()
    file.close()
    return key

#get master password
def getMasterPwd():
    file = open("password_manager/master_password.txt","r")
    master = file.read()
    file.close()
    return master

#limit number of login attempts to 3
count = 1
while count <= 3:
    master_pwd = input("Enter master password? ")
    root_pwd = getMasterPwd()
    if root_pwd != master_pwd:
        if count < 3:
            print("Wrong Password Retry!")
            count += 1
            continue
        elif count == 3:
            print("ENTERED WRONG PASSWORD 3 TIMES, TRY AGAIN LATER!")
            quit()
    else:
        print(f"LOGIN SUCCESSFUL, WELCOME!")
        break


key = load_key() + master_pwd.encode()
fer = Fernet(key)

#functions to manipulate password.txt file
def view():
    with open('password_manager/passwords.txt','r') as fObj:
        for line in fObj.readlines():
            data = line.rstrip()
            user , password = data.split("|")
            print(f"account: {user}, password: {fer.decrypt(password.encode()).decode()}") #decrypt password
               

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open('password_manager/passwords.txt','a') as fObj:
        fObj.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n") #encrypt password

#loop to ask user what they want to be done 
while True:
    userinput = input("Do you want to view existing passwords or add a new password. (view(v), add(a), quit(q)): ")
    if userinput.upper() == 'Q':
        print("You Quitted!")
        quit()
    if userinput.upper() == 'A':
        add()
    elif userinput.upper() == 'V':
        view()
    else:
        print("Please enter a valid option!")
