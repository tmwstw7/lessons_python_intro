import argparse

def simple(a, b):
    if isinstance(a, int) and isinstance(b, str):
        print('ok')


def divider(a, b):
    print(a / b)


"""
__name__ 
1) __main__ в случае когда мы работаем с файлом напрямую
2) Имя файла/модуля, если мы файл импортируем
"""

my_parser = argparse.ArgumentParser()

my_parser.add_argument('a',
                       help="first arg",
                       type=int)
my_parser.add_argument('b',
                       help="second arg",
                       type=int)
my_parser.add_argument('b',
                       help="second arg",
                       type=int)

# ограничиваем выполнение всего в теле иф во время импортов
if __name__ == "__main__":
    args = my_parser.parse_args()
    print(args.a, type(args.a))
    print(args.b, type(args.b))
    divider(args.a, args.b)





