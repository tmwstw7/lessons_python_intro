# tuples
tup_1 = tuple([1,2,3,4])
tup_2 = 9, 0, 77, 2
tup_3 = (4, 5, 6, 8)

# print(tup_3, type(tup_3))

# print(tup_3 * 3)
# print(tup_1 + tup_2)
# tup_4 = (1,2,3, (4,5,6))
# print(tup_4[3][0])

## Stings, List, Tuple

# print(tup_1.count(3))

# a = 1, 2, 547, 6, 'fds'













# Dicts

fruits = {'apples': 7,
          'oranges': (1, 2, 3, 4),
          'bananas': "7",
          'tropical': {'guava': [1,2,3,4],
                       'batat': 10}}

# print(fruits.items())

# fruits_2 = dict([('apples', 7), ('oranges', (1, 2, 3, 4)), ('bananas', '7')])

# print(fruits['tropical']['guava'][-1])

# print(fruits.get('tomatoes', 'No tomatoes :('))

# fruits['apples'] *= 2
# fruits['lemons'] = 100
# print(fruits)

d = {}

d[1] = 1.1
d[2] = 2.2

d.update(x="jdsghjk",
         y=[1,2,4,5],
         z=300)
# print(d)

# d.clear()

# print(d)

# pop = d.pop('x')

# print(d)
# print(pop)

del d['x']

# print(d)








# # sets
#
# list_1 = [1,1,1,1,1,12,2,2,12, 3,3,3]
# print(list_1)

# print(set(list_1))

# str_1 = "Hello World"
# set_1 = set([1,2,3,4])
# set_2 = set([1, 1, 7, 8, 4, 4, 6])
# print(set_1)
# print(set_2)
# print(set_1 == set_1)

# print(len(set_1))
# print(list(str_1))
# print(tuple(str_1))
#
# set_2 = {}
# print(type(set_2))
# print(set_1.difference(set_2))

# While loop
# i = 5
# while True:
#     print(i)
#     i += 2


# For

list_1 = [1,2,3,4,5,6,7]
str_1 = 'Hello Word'
dict_1 = {'o': 3, 'y': 9, 'p': 55}

for key, value in dict_1.items():
    print(key, value)
    print()












