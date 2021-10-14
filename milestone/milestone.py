import time
import ast
from types import new_class

def password_isvaid(password):
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
    else:
        isValid=True
        
    return isValid
        

def write_to_file(data, username=None):
    if username is not None:
        note = f'milestone/notes/{username}.txt'
        with open(note, 'w') as note_file:
            note_file.write(data)
        return
    
    file = 'milestone/users.txt'
    with open(file, 'w') as doc_file:
        doc_file.write(f'{data}')
    return
        
    

def read_file_data(name=None):
    
    if name is not None:
        user_note = f'milestone/notes/{name}.txt'
        try:
            with open(user_note, 'r') as file:
                notes = file.read()
                
                return notes
        except Exception as e:
            return False
       
    user_file = 'milestone/users.txt'
    
    with open(user_file, 'r') as users:
        user_data = ast.literal_eval(users.read())
    
    return user_data

user_data = read_file_data()

keep_running = True

while keep_running:
    user_activity = input("Enter s to signup, l to login and anyother key to quit\n>>").lower()
    if user_activity=='s':
        name = input("Full Name:\n>>")
        username = input("Enter a username:\n>>")
        email = input("Enter a email:\n>>")
        pin = input("Enter password:\n>>")
        
        print("Validating username...")
        time.sleep(2)
        if username in user_data.keys():
            print("Username already exists. Try again")
            continue
        print("validating password...")
        time.sleep(2)
        if password_isvaid(pin):
            data = [('name', name), ('pin', pin), ('email', email)]
            user_data[username] = {}
            user_data[username].update(data)
        else:
            continue  
        
        
        print(f"Your account has been successfully activated.\n\n")
        
        
    elif user_activity=='l':
        print("Enter login details below".title())
        username = input("Username:\n>>")
        pin = input("Password:\n>>")
        
        user_details = user_data.get(username, False)
        if user_details and user_details.get('pin')==pin:
            logged_in=True
            while logged_in:
                action = input(f"""Welcome, {user_details.get('name')}!
What would you like to do?
    1 for View Profile
    2 for Create Note
    3 for View Note
Press any other key to logout\n>>""").lower()
                if action == '1':
                    print("Here is your profile!")
                    print(f"Name: {user_details['name']}\nEmail: {user_details['email']}")
                    
                    edit = input("Do you wish to edit your profile?y/N\n>>").lower()
                    if edit == 'y':
                        where = input('Enter a to edit your name, b to edit your email and c to change your password\n>>')
                        
                        if where == 'a':
                            new_name = input("Enter Full name:\n>>")
                            user_details['name'] = new_name
                            
                        elif where == 'b':
                            new_email = input("Enter new email:\n>>")
                            user_details['email'] = new_email
                        elif where == 'c':
                            new_password = input("Enter new passowrd:\n>>")
                            user_details['pin'] = new_password
                elif action == '2':
                    print("Please wait while your note is being created")
                    time.sleep(4)
                    content = input("Enter note contents:\n>>")
                    write_to_file(content, username)
                    print("Note successfully saved.")
                    
                        
                elif action == '3':
                    user_note = read_file_data(username)
                    
                    if user_note == False:
                        print("You currently have no notes. Plese add one")
                        
                    else:
                        print(user_note)
                    
                        edit = input('Enter e to edit your note or c to clear. Press any other key to continue\n>>')
                        if edit == 'e':
                            print("Note that editing this note overwrites the original content. Copy your contents to a safe place before proceeding.")
                            content = input("Enter edited contents:\n>>")
                            write_to_file(content, username)
                        elif edit == 'c':
                            write_to_file("", username)
                        
                else:
                    break    
                
        else:
            print("Please enter a valid username and password")
            tryagain = input("Did you forget your password?y/N\n>>")
            if tryagain=='y':
                username = input("Enter your username\n>>")
                if username in user_data.keys():
                    full_name = input("Please enter your full name to verify identity\n>>")
                    fullname = user_data.get(username)['name']
                    if full_name==fullname:
                        new_password = input("Enter new password\n>>")
                        if password_isvaid(new_password):
                            user_data[username]['pin'] = new_password
                            print("Password reset succesful")
                        else:
                            continue
            else:
                continue

    else:
        print("Sorry to see you go.")
        break

# write_to_file('transaction',transaction_record)
write_to_file(user_data)
