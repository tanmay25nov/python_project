
user_name= input("enter user name: ")
user_pwd= input("Please enter a password: ")
user_error="there is an error in Password"
user_pwd_check_1= "False"
user_pwd_check_2= "False"
user_pwd_check_3= "False"
user_pwd_check_4= "False"

# Check if password contains at least one digit, uppercase letter, lowercase letter, and special symbol and min length
def check_password_strength(passw):
    global user_pwd_check_1
    global user_pwd_check_2
    global user_pwd_check_3
    global user_pwd_check_4
    global user_error

    if (len(passw)>=8):
        
        for i in range (0,len(passw)):
            if ord(*passw[i])>=48 and ord(*passw[i])<=57:
                user_pwd_check_1 = "True" 
                                  
            elif ord(*passw[i])>=65 and ord(*passw[i])<=90:
                user_pwd_check_2 = "True"
                  
            elif ord(*passw[i])>=97 and ord(*passw[i])<=122:
                user_pwd_check_3 = "True"
            
            elif (ord(*passw[i])>=33 and ord(*passw[i])<=38) or ord(*passw[i])==42 or ord(*passw[i])==64 or ord(*passw[i])==95:
                user_pwd_check_4 = "True"
                        
            else:
                user_error = ("This special character is not allowed")
                return False
                break
# below statement to check if all condition of password is satisfying or not
        if user_pwd_check_1 == "False":
            user_error = "Min One digit missing in password"
            return False
        elif user_pwd_check_2 == "False":
            user_error = "Min One Capital Letter missing in password"
            return False
        elif user_pwd_check_3 == "False":
            user_error = "Min One Small Letter missing in password"
            return False
        elif user_pwd_check_4 == "False":
            user_error = "Special character is missing"
            return False
        
        if user_pwd_check_1 == "True" and user_pwd_check_2 == "True" and user_pwd_check_3 == "True" and user_pwd_check_4 == "True":
            return "True"
    else:
        user_error=("Password length is less then 8 character")
        return False
        
if check_password_strength(user_pwd):
    print(f"The User name is : {user_name} ")
    print("The Password is valid and updated...") 
else:
    print(f"Error: The Password is not valid and {user_error}")
