import random
import time
import ast

def write_to_file(type, data):
    if type == 'customer':
        file = 'bankapp_v3/customers.txt'
    elif type == 'transaction':
        file = 'bankapp_v3/transactions.txt'
        
    with open(file, 'w') as doc_file:
        doc_file.write(f'{data}')
    

def read_file_data():
    trans_file = 'bankapp_v3/transactions.txt'
    customer_file = 'bankapp_v3/customers.txt'
    
    with open(customer_file, 'r') as customer:
        cus_data = customer.read()
        customer_data = ast.literal_eval(cus_data)
    with open(trans_file, 'r') as transaction:
        trans_data = transaction.read()
        transaction_data = ast.literal_eval(trans_data)   

    return customer_data, transaction_data

user_data, transaction_record = read_file_data()

keep_running = True


def update_transaction_record(amount, trans_type, transaction, account_num):
    """This function takes in the amount and other transaction details. Then it updates the transaction dictionary. It doesn't return anything."""
    
    trans_data = {
        'amount':amount,
        'trans_type':trans_type,
        'transaction':transaction
        }
                        
    transaction_record[account_num].append(trans_data)

def generate_acc_num():
    num = [str(i) for i in range(10)]
    acc = ['9']
    acc.extend([random.choice(num) for i in range(9)])
    account_num = "".join(acc)
    
    if account_num in user_data.keys():
        return generate_acc_num()
    
    return account_num

while keep_running:
    user_activity = input("Enter s to signup, l to login and anyother key to quit\n>>").lower()
    if user_activity=='s':
        name = input("Name:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
        account_num =generate_acc_num()
        data = [('name', name), ('pin', pin), ('balance', 0)]
        user_data[account_num] = {}
        user_data[account_num].update(data)
        
        #create empty transaction record
        
        transaction_record[account_num] = []
        
        print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.\n\n")
        
        
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
                        
                    
                    else:
                        account_details['balance']-=amount
                        print('Please take your cash')
                        
                        #save transaction detail
                        update_transaction_record(amount,"Debit", "Withdrawal", account_num)
                        
                elif action == 'd':
                    amount = float(input("Enter amount to deposit\n>>"))
                    
                    
                    account_details['balance']+=amount
                    print('Deposit complete')
                    
                    #save transaction detail
                    update_transaction_record(amount,"Credit", "Deposit", account_num)
                        
                      
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
                        
                            update_transaction_record(amount,"Debit", "Transfer", account_num)
                        
                            recepient['balance']+=amount
                            
                            #save transaction detail
                        
                            update_transaction_record(amount,"Credit", "Transfer", recepient_account)
                            
                            print("Transfer successful. Gerrout!")
                            
                    else:
                        print('No active customer for this account number. Gerrout!')
                        
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

write_to_file('transaction',transaction_record)
write_to_file('customer',user_data)
