import random
import time

user_data = {}
transaction_record = {}
keep_running = True


while keep_running:
    user_activity = input("Enter s to signup, l to login and anyother key to quit\n>>").lower()
    if user_activity=='s':
        name = input("Name:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
        num = [str(i) for i in range(10)]
        acc = ['9']
        acc.extend([random.choice(num) for i in range(9)])
        account_num = "".join(acc)
        data = [('name', name), ('pin', pin), ('balance', 0)]
        user_data[account_num] = {}
        user_data[account_num].update(data)
        
        #create empty transaction record
        
        transaction_record[account_num] = []
        
        print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.")
        
        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
        if progress == 'p':
            continue
        else:
            break
    elif user_activity=='l':
        print("Enter login details below".title())
        account_num = input("Account num:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
        account_details = user_data.get(account_num, False)
        if account_details and account_details.get('pin')==pin:
            logged_in=True
            while logged_in:
                action = input(f"""Welcome, {account_details.get('name')}!
What would you like to do?
    a for account statement
    b for balance
    d for deposit
    t for transfer
    w for withdrawal
Press any other key to logout\n>>""").lower()
                if action == 'w':
                    amount = float(input("Enter amount to withdraw\n>>"))
                    
                    if amount >= account_details.get('balance', 0):
                        time.sleep(2)
                        print("Insufficiant funds")
                        
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                    else:
                        account_details['balance']-=amount
                        print('Please take your cash')
                        
                        #save transaction detail
                        
                        trans_data = {
                            'amount':amount,
                            'trans_type':'Debit',
                            'transaction':'Withdrawl'
                        }
                        
                        transaction_record[account_num].append(trans_data)
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                elif action == 'd':
                    amount = float(input("Enter amount to deposit\n>>"))
                    
                    
                    account_details['balance']+=amount
                    print('Deposit complete')
                    
                    #save transaction detail
                        
                    trans_data = {
                        'amount':amount,
                        'trans_type':'Credit',
                        'transaction':'Deposit'
                    }
                    
                    transaction_record[account_num].append(trans_data)
                        
                    progress = input("Enter p to do something else and any key to logout.\n>>").lower()
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
                            #save transaction detail
                        
                            trans_data = {
                                'amount':amount,
                                'trans_type':'Debit',
                                'transaction':'Transfer'
                            }
                            
                            transaction_record[account_num].append(trans_data)
                        
                            recepient['balance']+=amount
                            
                            #save transaction detail
                        
                            beneficiary_trans_data = {
                                'amount':amount,
                                'trans_type':'Credit',
                                'transaction':'Transfer'
                            }
                            
                            transaction_record[recepient_account].append(beneficiary_trans_data)
                            
                            print("Transfer successful. Gerrout!")
                            progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                            if progress == 'p':
                                continue
                            else:
                                break
                    else:
                        print('No active customer for this account number. Gerrout!')
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                elif action == 'b':
                    print(f"Your current balance is NGN{account_details['balance']}\n")
                    
                elif action == 'a':
                    
                    if len(transaction_record[account_num]) > 0:
                        last_5_transactions = transaction_record[account_num][-5:]
                        print("Here is your last 5 transactions")
                        for transaction in last_5_transactions:
                            print("Amount: ", transaction['amount'])
                            print("Transaction Type: ", transaction['trans_type'])
                            print("Transaction Ref.: ", transaction['transaction'])
                            print()
                    else:
                        print("You have not made any transactions. Please make a transaction.")
                        
                else:
                    break    
                
        else:
            print("Please enter a valid account number and pin")

    else:
        print("Sorry to see you go.")
        break


print(user_data)
print(transaction_record)








# x = 0
# for i in range(10):
#     print(i, '\n')
#     for j in range(-1, -10, -1):
#         print(j, '\n')
#         x += 1

# print(x)

# for num in range(-2,-5,-1):
#     print(num, end=", ")


# x = 0
# while (x < 100):
#   x+=2
# print(x)

# if -3:
#     print("a")
# else:
#     print("b")