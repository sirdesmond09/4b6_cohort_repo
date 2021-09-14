# print("Beautiful" + " City")


# name = "Joy"
# price = 20
# print(f"Welcome {name}. You are to pay NGN{price}")


# name = input("Tell us who you are: ")
# print("Welcome {}.\nYou have just signed in.\n\tSigned\n\tManagement".format(name.title()))

# name = input("What is your name? ")
# age = int(input("Tell us your age: "))

# yob = 2021 - age

# print(f"Hello, {name}. You were born in {yob}")

# print('Her father\'s daughter')



# name = "MY FILE.PDF".upper()
# print(name)

# print(name.endswith("pdf"))

# print(name.find('file'))
# print(name.index('file'))


# s = "LJDNF;VSJDFN"

# print(s.isupper())


# fullname = "Desmond Nnebue Chu"
# name_list = fullname.split()
# print(name_list[2])

# word_list = ['Desmond', 'Nnebue', 'Chu']

# joined = "-".join(word_list)
# print(joined)

# word = "I am a boy"

# new_word = word.replace(" ", "-")

# print(new_word)

word = """This is a class about django.
I love to write django.
Django is cool""".lower()

user_input = input("Enter your word:\n>").lower()

print(f"{word.count(user_input)} found")

my_word =  word.replace(user_input, user_input.upper())

print(my_word)