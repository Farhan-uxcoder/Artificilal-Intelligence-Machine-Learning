username = input("Enter the username : ")
password = input("Enter the password : ")

if(username == "admin" and password == "pass"):
    print("Successfully loged in")
else:
    if username != "admin":
        print("invalid input")

