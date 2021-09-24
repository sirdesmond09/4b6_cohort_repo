# # s1 = "AULT"
# # s2 = "kELLY"
# # s3 = int(len(s1)/2)
# # solution = s1[0:s3] + s2 + s1[s3:]
# # print(solution)

# s1 = "China"
# s2 = "Japan"
# a = s1[0]
# b = s2[0]
# c = s1[len(s1)//2]
# d = s2[len(s2)//2]
# e = s1[-1]
# f = s2[-1]
# solution = a+b+c+d+e+f
# print(solution)

# s1 = 'ABC' ; s2= 'XYZ'
# output= s1[0] + s2[-1] + s1[1]+ s2[-2]+ s1[-1]+ s2[0]
# print(output)



# username = ["frank2","henry"]
# first_name = input("Enter first name:\n>")
# last_name = input("Enter last nme:\n>")
# userid = last_name[:3] + first_name[-2:]
# username.append(userid)
# print(userid)
# output = "Hello, " + first_name.title() + "\nThank you for signing up. Your account has successfully been created\nYour account id is " + userid + "\n\tCheers\n\tAdmin"
# print(output)
# print(username)

# a = [500,200,[200,500,700,[250,800],250],[1000]]

# soln = a[2]
# soln700 = soln[2]
# print(soln700)

# solnn = soln[3]
# soln800 = solnn[1]
# print(soln800)


# solution = soln800 + soln700


# a[3].append(solution)
# print(a)


# a = "Emma is a data scientist and he loves python. Emma works at google"
# print(a.index("Emma"))
# print(a.rindex("Emma"))


# list_ = [49, 17, 27, 32, 19, 37, 22, 48, 0]
# list_.sort()
# print(list_)
# list_.reverse()
# print(list_)

# print(list_)

# import random
# a = ["f", 'k', 't', 's', 'o', 'p', 'e', 'j', 'm']
# grp1 = []
# grp2 = []
# count = 1
# for i in a:
    
#     random.shuffle(a)
#     choice = random.choice(a)
#     if count % 2 != 0:
#         grp1.append(choice)
#     else:
#         grp2.append(choice)
#     a.remove(choice)
    
    
# print(grp1)


# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))


# print(type(range(5)))

# x = 75
# def myfunc():
#     x = x + 1
#     print(x)

# myfunc()
# print(x)

# str1 = 'Ault\'Kelly'
# print(str1)

# str1 = "PYnative"
# print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])


# print("welcome to the beautiful world of python".title())

# str1 = 'Welcome'
# print(str1*2)

# str1 = "my isname isisis jameis isis bond";
# sub = "is";
# print(str1.count(sub, 4))

# l = [None] * 10
# print(type(None))

# sampleList = [10, 20, 30, 40]
# del sampleList[0:6]
# print(sampleList)

# aList = [5, 10, 15, 25]
# print(aList[::2])

# resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
# print(resList)

import timeit


arr = [-1, 4, 2, -6, -6, -1, -8, 9, 0, -4, -9, -2, -6, 9, -6, -4, 5, -7, 0, 5, 0, -6, -3, 4, 6, 0, 6, -1, -5, -10]
pos = 0
neg = 0
zero = 0

for i in arr:
    if i > 0:
        pos+=1
    elif i < 0:
        neg+=1
    else:
        zero+=1
        
pos_ratio = pos/len(arr)
neg_ratio = neg/len(arr)
zero_ratio = zero/len(arr)

print(round(pos_ratio, 6))
print(round(neg_ratio, 6))
print(round(zero_ratio, 6))
print(timeit.timeit())