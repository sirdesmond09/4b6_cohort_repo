# num_list = input("Enter a list of numbers:\n>").split(',')
# numbers= map(lambda string: int(string), num_list)
# print(sum(numbers))
# print(sum(numbers)/len(numbers))

import random

# user = input("Enter your name:\n>")
# print("creating account, please wait...")
# time.sleep(3)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('Almost there...')
# time.sleep(2)
# print(f"Welcome {user}, your account has been created!")

# my_list = [2,3,5,3,1,4,56,3]
# random.shuffle(my_list)
# print(random.sample(my_list, 3))
# print(my_list)

# random.seed(2)
# print(random.randrange(3,10))


# date = datetime.now()

# print(datetime.strftime(date,"%A, %d %B %Y"))
def random_nums(n):
    return [random.randrange(n) for i in range(n)]

print("Welcome to this game")
list_of_numbers=[96, 60, 55, 67, 65, 57, 82, 52, 16, 91, 60, 46, 70, 1, 6]
choice = int(input(f"Guess number from:\n{list_of_numbers}\n>>"))
random.shuffle(list_of_numbers)

com_choice = random.choice(list_of_numbers)

if choice==com_choice:
    print("You win")
else:
    print("E be like say you no win. Sorry ☹")
