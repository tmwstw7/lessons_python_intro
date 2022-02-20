names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']



# @timer
def recursion(items):
    count = 0

    for item in items:
        if isinstance(item, list):
            print(f"Vlozheniy spisok: {item}")
            count += recursion(item)
        else:
            print(f'Atomarnoe zhnachenie: {item}')
            count += 1

    return count

# print(recursion(names))


recursion(names)

def partition(array, low, high):

    # print(f"Array: {array}")
    pivot = array[high]
    # print(f"Opora: {pivot}")

    i = low - 1
    # print(f"i: {i}, array[i] = {array[i]}")

    for j in range(low, high):
        # print(f"j: {j}, array[j] = {array[j]}")
        if array[j] <= pivot:

            i += 1
            # print(f'New i: {i}')

            array[i], array[j] = array[j], array[i]
            # print(f"Modified array: {array}")
            # print()

    array[i + 1], array[high] = array[high], array[i + 1]
    # print(f"Final array after partition: {array}")
    # print()
    # print()

    return i + 1


def quick_sort(array, low, high):

    if low < high:  # <- ВЫХОД ИЗ РЕКУРСИИ (проверяем что индексы начала и конца не совпадают)

        part = partition(array, low, high)

        quick_sort(array, low, part - 1)
        quick_sort(array, part + 1, high)


# data = [-100, 7, 89, 0, 44, 1, 4.6]
# size = len(data) - 1
#
# print(f"Data: {data}")
# quick_sort(data, 0, size)
#
# print(data)




















