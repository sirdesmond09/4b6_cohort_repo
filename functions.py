# def mean(num):
#     return sum(num)/len(num)


# def median(num):
#     sorted(num)
#     if len(num)%2==0:
#         mid_point = len(num)//2
#         first = num[mid_point-1]
#         second=num[mid_point]
#         return (first+second)/2
#     else:
#         mid_point = len(num)//2
#         return num[mid_point]
    

# def mode(num):
#     freq = {}
#     for i in num:
#         if i in freq.keys():
#             freq[i]+=1
#         else:
#             freq[i]=1
#     print(freq)
#     max_key = max(freq, key=freq.get)
    
#     return max_key


# def std(num):
#     m = mean(num)
#     return ((sum([a-m for a in num]))**2/len(num))**0.5


# def variance(num):
#     st = std(num)
#     return st**2

# def prime(num):
#     if num <= 1:
#         return False
#     if num ==2:
#         return True
    
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# def prime_in_list(num):
#     return list(filter(lambda x: prime(x), num))


# print(prime_in_list([2,3,7,5,11,23,14]))

# myfile = open('mary.txt', mode='w')
# myfile.write("This is a new line that i just decided to write because I am a learner")

# texts = myfile.readlines()
# for text in texts:
#     print(text)

import ast

d = {
    "name":"paul"
}
with open('des.txt', 'w') as paul:
    paul.write(f'{d}')
    
with open('des.txt', 'r') as mercy:
    favour = mercy.read()
    a = ast.literal_eval(favour)
    print(type(a))
# paul.write("I have risen")