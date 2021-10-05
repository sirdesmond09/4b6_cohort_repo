import random
import time

user_data = {}
keep_running = True


while keep_running:
    user_activity = input("Enter s to signup and any other key to login\n>>").lower()
    if user_activity=='s':
        name = input("Name:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
        num = [str(i) for i in range(10)]
        account_num = "".join([random.choice(num) for i in num])
        data = [('name', name), ('pin', pin), ('balance', 0)]
        user_data[account_num] = {}
        user_data[account_num].update(data)
        print(user_data)
        print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.")
        
        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
        if progress == 'p':
            continue
        else:
            break
    else:
        print("Enter login details below".title())
        account_num = input("Account num:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
        account_details = user_data.get(account_num, False)
        if account_details and account_details.get('pin')==pin:
            action = input(f"""Welcome, {account_details.get('name')}!
What would you like to do?
    w for withdrawal
    d for deposit
    t for transfer
Press any other key to quit\n>>""").lower()
            if action == 'w':
                amount = float(input("Enter amount to withdraw\n>>"))
                
                if amount >= account_details.get('balance', 0):
                    time.sleep(2)
                    print("Insufficiant funds")
                    print("Session Expired")
                    
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
                else:
                    account_details['balance']-=amount
                    print('Please take your cash')
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
            elif action == 'd':
                amount = float(input("Enter amount to deposit\n>>"))
                
                
                account_details['balance']+=amount
                print('Deposit complete')
                progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                if progress == 'p':
                    continue
                else:
                    break   
            elif action == 't':
                amount = float(input("Enter amount to transfer\n>>"))
                recepient_account = input("Enter destination account number\n>>")
                
                recepient = user_data.get(recepient_account, False)
                if recepient:
                    if amount >= account_details.get('balance', 0):
                        print("Insufficient funds. GERROUT!")
                    else:
                        account_details['balance']-=amount
                        recepient['balance']+=amount
                        print("Transfer successful. Gerrout!")
                        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                else:
                    print('No active customer for this account number. Gerrout!')
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
                
                
        else:
            print("Please enter a valid account number and pin")


