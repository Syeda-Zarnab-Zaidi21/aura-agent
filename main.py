choice = 0 #initialie
users={} #empty dictionary
while choice != 3: # condition
    print("Welcome To AURA.\n1. Sign Up\n2. Sign In\n3. Exit")
    choice = int(input("Enter a Number:")) #input

    #Sign up
    if choice==1:
        print("Sign up")
        username=input("Username: ")
        if username in users:
            print("This username is already registered.Try another")
        else:
            print("Username is availaible")

            email=input("Email: ")
            password=input("Password")
            confirm_password = input("Confirm Password: ")
            if password==confirm_password:
              users[username]=[email,password]
              print("Saved Succesfully")
            else:
                print("Password not match")
                
                
            
#Sign In 
    elif choice==2:
        print("Sign In")
        username=input("Enter username : ")
        if username in users:
            password=input("Enter your password : ")
            if password==users[username][1]:
                print("Login Successfully")
            else:
                print("Incorrect Password")
        else:
            print("Username not found")
            
    elif choice==3:
        print("Exit")
    else:
        print("Invalid Choice")
    
    

