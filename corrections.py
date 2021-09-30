### Assignment on SET
# students_in_A = set(input().split())
# students_in_B = set(input().split())

# list_of_intersected_students = students_in_A.intersection(students_in_B)

# print(list_of_intersected_students)
# print(len(list_of_intersected_students))


### ROCK PAPAER SCISSORS
# import random

# print("Welcome to the Game")
# print("Rock Paper Scissors")

# help = """
# This is a simple game that follows the rule below:
# Rock wins Scissors
# Paper wins Rock
# Scissors wins Paper

# choices are R for rock, P for paper and S for scissors

# You have only one chance. Can you beat me?
# """

# print(help)

# player_choice = input("what do you choose?\n>").lower()
# choices = ['r', 'p', 's']
# random.shuffle(choices)
# com_choice = random.choice(choices)

# if player_choice in choices:
#     if (player_choice=='r' and com_choice=='s') or (player_choice=='p' and com_choice=='r') or (player_choice=='s' and com_choice=='p'):
#         print('You win')
        
#     elif (com_choice=='r' and player_choice=='s') or (com_choice=='p' and player_choice=='r') or (com_choice=='s' and player_choice=='p'):
#         print('computer win')
#     else:
#         print("It's a tie")
        
# else:
#     print("Invalid input. You lose!")
    

#Assignment 3

# import re
# password = input("Input a password\n>")
# x = True

# while x:
#     if(len(password)<6 or len(password)>16):
#         break
#     elif not re.search("[A-Z]", password):
#         break
#     elif not re.search("[a-z]", password):
#         break
#     elif not re.search("[0-9]", password):
#         break
#     elif not re.search("[@#$]", password):
#         break
#     else:
#         print("Valid password")
#         x= False
        
# if x:
#     print("invalid password")
# special_char = ['@', '$', '#']
# isValid = True

# if len(password) < 6:
#     print("Password length should not be less than 6")
#     isValid = False
# if len(password) > 16:
#     print("Password length should not be more than 16")
#     isValid = False
# if not any(char.isdigit() for char in password):
#     print("Password should contain at least a number")
#     isValid = False
# if not any(char.islower() for char in password):
#     print("Password should contain at least a lowercase letter [a-z]")
#     isValid = False
# if not any(char.isupper() for char in password):
#     print("Password should contain at least a uppercase letter [A-Z]")
#     isValid = False
# if not any(char in special_char for char in password):
#     print("Password should contain at least a special character [@$#]")
#     isValid = False
# if isValid:
#     print("Password is valid")
# else:
#     print("Invalid Password")





# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# for x, y in zip(list1, list2):
#     print(x, y)

import time
user_data = {}
setup = True

while setup:
    activity = input("Login or Sign up?\n>>").lower()

    if activity == 'login':
        email    = input("Enter your email\n>>")
        password = input("Enter your password\n>>")
        
        time.sleep(2)
        if email in user_data.keys():
            actual_password = user_data.get(email)

            if actual_password == password:

                print('Login successful')
                break
            else:
                print("Plese enter a valid email and password.")
        else:
            print("There is no active user with this email")    

    elif activity == 'signup':
        signup=True
        while signup:
            email    = input("Enter your email\n>>")
            password = input("Enter your password\n>>")
            re_password = input("Confirm password\n>>")
            special_char = ['@', '$', '#']
            isValid = True

            if password != re_password:
                print('Please enter matching passwords')
                continue
            if (len(password) < 6) or (len(password)>16):
                print("Password length should not be less than 6")
                isValid = False
            elif not any(char.isdigit() for char in password):
                print("Password should contain at least a number")
                isValid = False
            elif not any(char.islower() for char in password):
                print("Password should contain at least a lowercase letter [a-z]")
                isValid = False
            elif not any(char.isupper() for char in password):
                print("Password should contain at least a uppercase letter [A-Z]")
                isValid = False
            elif not any(char in special_char for char in password):
                print("Password should contain at least a special character [@$#]")
                isValid = False
                continue
            else:
                user_data[email] = password
                print(user_data)
                signup=False
        con = input("Press 'y' to continue and any other key to quit\n>>").lower()
        if con == 'y':
            continue
        else:
            setup=False
    else:
        print("Please select a valid option")


# x = 10
# while x > 0:
#     print(x)
#     x-=1

# x = True   
# while x:
#     print("I am a boy")
    
#     x=False