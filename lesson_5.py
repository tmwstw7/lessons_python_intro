# For loop revision
list_1 = [1111,242,365 ,4908]
# list_2 = [11,2995,7865 ,48]

# list_2 = []
# for i in list_1:
#     list_2.append(i**2)

# Generators
# List comprehention
# list_2 = [str(i)*10 for i in list_1]
# print(list_2)

# dict_1 = {lol: lol**3 for lol in list_1}
# print(dict_1)

gen = (str(i)*10 for i in list_1)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# print(list(gen))


# group fucs


# a = range(1, 11, 2)
# for i in sorted(list_1):
#     print(i)
#
# print(list_1)

# print(dict(zip(list_1, list_2)))
# z = dict(zip(list_1, list_2))
# dict_2 = {str(j): str(i*2) for i, j in zip(list_1, list_2)}
# print(dict_2)

# list_3 = ['a', 'b', 'c', 'd', 'r']
# print(len(list_1), len(list_3))
# print(list(zip(list_1, list_3)))

# print(list(reversed(list_1)))


# if / elif / else

# number = 19191

# if number // 3:
#     print("Yes, it is!", number // 3)


# for i in list_1:
#     print(f"Current element: {i}")
#     if (i % 2 == 0 and i % 5 == 0) \
#             or (i % 3 == 0 and i % 4 == 0):
#         print('Yeee', i)
    # elif i % 5 == 0:
    #     print('Yeee 2x', i)
    # elif i % 5 == 0:
    #     print('Yeee 2x', i)
    # else:
    #     print('To bad')

# print(all(i % 1 == 0 for i in list_1))
# print(any(i % 2 == 0 for i in list_1))
# print(22 in list_1)

# if 22 in list_1:
# #     print('Wow')
# #     if any(i % 2 == 0 for i in list_1):
# #         print('wow 2')
# # else:
# #     print('Sad :(')
strings = ['apples', 'bannanas', 'berries', 'orange']

# many = [i for i in strings if i.endswith('s')]
# print(type(strings) == list)
print(all(isinstance(i, str) for i in strings))
