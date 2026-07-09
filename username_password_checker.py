correct_username = "Touqu007"
correct_password = "Password00"

max_attempt = 3
attempt = 0

while attempt < 3:   
    user_name = input("Enter Your User Name Here : ")
    pass_word = input("Enter Your Password Here : ")
    attempt += 1

    if user_name == correct_username and pass_word == correct_password :
        print("     ===.Logged In Sucessfully.===     ")
        break   
    else :
        print("***.User Name OR Password Is Incorrect.***")
        print(f"You have {max_attempt - attempt} More Attempts Reamaining ")