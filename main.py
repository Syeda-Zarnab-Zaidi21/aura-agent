import tasks
choice = 0 #initialie
users={} #empty dictionary
while choice != 6: # condition
    print("\n===== AURA =====")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Add Task")
    print("4. View Tasks")
    print("5. Delete Task")
    print("6. Exit")
    #Exception Handling
    try:
            choice = int(input("Enter a Number:"))
    except ValueError:
            print("Please enter a number from 1 to 6.")
            continue


    #Sign up
    if choice==1:
        print("Sign up")
        #created variable for username
        username=input("Username: ")
        if username in users:
            print("This username is already registered.Try another")
        else:
            print("Username is availaible")
#Create variable for email
            email=input("Email: ")
            #Created Variable for Password
            password=input("Password")
            #Password Validation
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
#Add Task
    elif choice==3:
        tasks.add_task()

    #View Task
    elif choice==4:
        tasks.view_tasks()
        

    # Delete Tasks
    elif choice==5:
        tasks.delete_tasks()
    
# exit         
    elif choice==6:
        print("Exit")
    else:
        print("Invalid Choice")
    
    

