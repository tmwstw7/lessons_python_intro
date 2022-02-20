# import math
# import random

#
# def prorab(function_to_wrap):
#     def wrap_func(smeta):
#         print(f"Init smeta: {smeta}")
#         smeta = [math.ceil(i) for i in smeta]
#         function_to_wrap(smeta)
#     return wrap_func


# @prorab
# def funk_1(smeta):
#     print(f"Smeta: {smeta}")

#
# smeta = [round(random.uniform(10.0, 100.0), 2) for _ in range(11)]

# funk_1(smeta)

# a, _, b = (1, 2, 3)
# print(a,b)

# print(round(random.uniform(10.0, 100.0)))
# # print(len(str(random.uniform(10.0, 100.0)).split('.')[-1]))


"""
int main(){

}
"""
# def funk():
#     # print(1 / 0)
#     l = [1,2,4,5]
#     print(l[10])
#
# funk()

# try:
#     a = [1, 2, 3, 4]
#     print(a[111])
#     print('No error!')
# except Exception:
#     print("We got an error!")
# else:
#     print('We got else')
# finally:
#     print('It works')

# def func_2(a):
#     if not isinstance(a, str):
#         raise TypeError('WE WANT STRING AS ARG!')
#     print(f"First and last symbols{a[0], a[-1]}")
#
#
# func_2('HELLO')


# f = open('text.txt', 'r')
# # print(f.read())
# for line in f:
#     print(line)

# f = open('text2.txt')
# # print(f.read())
# f.write('gfdhgh')
# f.close()
#
# with open('text2.txt', 'w') as f:
#     print(f.read())
#
# print()


a = 'Hello'

for i in dir(a):
    print(i)














