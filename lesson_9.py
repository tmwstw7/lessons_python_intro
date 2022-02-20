array_1 = [100, -1, 77, 3, -64, 23, 3, 8, 3, 4.5, -1.1]

import time


def timer(func):
    def w(args):
        start = time.time()
        func(args)
        end = time.time()
        print(end - start)
    return w


@timer
def bubble_sort(array):
    length = len(array)

    for i in range(0, length):
        # array[i + 1]
        for j in range(0, length - i - 1):
            # print(f"array[j]: {array[j]} <--> array[j + 1]: {array[j + 1]}")
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        # print()


bubble_sort(array_1)
# print(array_1)


def selection_sort(array):
    for step in range(len(array)):
        min_idx = step
        print(f"Min element: {array[min_idx]}")

        for i in range(step + 1, len(array)):
            print(f"array[i]: {array[i]} <--> array[min_idx]: {array[min_idx]}")
            if array[i] < array[min_idx]:
                min_idx = i

        print()
        array[step], array[min_idx] = array[min_idx], array[step]


# selection_sort(array_1)
# print(array_1)


def insertion_sort(array):
    print(array)
    for step in range(1, len(array)):
        key = array[step]
        print(f"Key: {key}")

        j = step - 1
        print(f"Left neig index: {j}")

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


# insertion_sort(array_1)
# print(array_1)



def linear_search(array, el):
    for i in range(0, len(array)):
        if array[i] == el:
            return i

    return -777

# print(array_1)
#
# result = linear_search(array_1, 0)
# print(result)
# print(array_1.index(0))

















