fruits = ['apples', 'bananas', 'berries', 'orange']
new_list = [1, 3, 5, 46, 57, 78, 989, 9]


# funcs

def function_0(k):
    print(k)


def function_2(k):
    print([i * 2 for i in k])


def function_1(sequence, suffix=''):
    return [i + suffix for i in sequence]


# def function_3(**kwargs):
#     print(kwargs)


def gen(sequence):
    for i in sequence:
        return i * 2


funcs = {
    '1': function_1,
    '2': function_2
}

# print(funcs['1'](fruits, '.com'))

# a = gen(fruits)
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# function_3(x=1, y=2, n='hjgfdb')
# print(function_1(fruits, '.com'))


# function_1(new_list, 7)

# # a = [i for i in range(10)]
# #
# function_1(, function_2)


# result = function_1(new_list, 10)
#
# print(f"Result: {result}")


# function_1(new_list)
# function_1(fruits)


    # p = 111
    # i = 0
    # for fruit in fruits:
    #     i += 1
    #
    # return str(i), float(p)

# print(function_1(fruits))
# len(fruits)












# lambdas

very_first_lambd = lambda x, y: x + y

# print(very_first_lambd(1, 1))

list_of_tuples = [('a', -111),
                  ('b', 756),
                  ('c', 33)]

# print(sorted(list_of_tuples, key=lambda x: x[1]))



# map

# map(what_to_do, sequence)

m = map(lambda x: f'{x}.com', fruits)
# s = [f"{i}.com" for i in fruits]

# print(list(m))
# print(s)

# filter(what_to_do, sequence)

list_0 = ['one', 'two', 'list', '', 'dict', '100', '1', '50', 1, 2, 4]

f = filter(lambda x: isinstance(x, int), list_0)

print(list(f))
