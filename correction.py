# my_list = ['this', True, 'student', 45, 66.43]
# cloned_list = my_list.copy()
# # print(cloned_list)

# Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# a = Sample_List.pop(0)
# print(Sample_List)
# b = Sample_List.pop(4)
# print(Sample_List)
# c = Sample_List.pop(-1)
# print(Sample_List)

# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# user_colour = input('Enter your favourite colour:\n')
# color_list.append(user_colour)
# print(color_list)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# print(list1)
# list1[2][2].extend([7000])
# print(list1)


# first = "John"
# second = "Bull"

# first, second = second, first

# print(first)

# aTuple = ("Orange",)
# print(type(aTuple))


# a = {"True", "Born", 50, "Water"}
# b = {"Mary", "Favour", "Tunde", 50}
# # s.add("Johnson")
# # print(s)

# # u = a.union(b)
# # print(u)
# # a.update(b)
# # print(a)

# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))


import timeit
from decimal import Decimal

# starttime = time.time()
arr = [-1, 4, 2, -6, -6, -1, -8, 9, 0, -4, -9, -2, -6, 9, -6, -4, 5, -7, 0, 5, 0, -6, -3, 4, 6, 0, 6, -1, -5, -10]
pos = []
neg = []
zero = []

for i in arr:
    if i > 0:
        pos.append(i)
    elif i < 0:
        neg.append(i)
    else:
        zero.append(i)
        
pos_ratio = len(pos)/len(arr)
neg_ratio = len(neg)/len(arr)
zero_ratio = len(zero)/len(arr)

print(round(Decimal(pos_ratio), 6))
print(round(Decimal(neg_ratio), 6))
print(round(Decimal(zero_ratio), 6))
print(timeit.timeit())


