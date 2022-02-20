def merge_sort(array):
    if len(array) > 1: # vihod iz recursii

        # print(f"Array: {array}")
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # print(f"r: {r}\nL: {L}\nM: {M}")
        # print()

        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        #     print(f"Changed array: {array}")
        #     print(f"k: {k}")
        # print("________________\n")

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            # print(f"Ostatki: {array}")

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            # print(f"Ostatki 2: {array}")



# data = [-100, 5, 1, 12, 0, 6.7]
#
# merge_sort(data)
#
# print(data)


"""
1 3 -10 6 8  .... 1000n ....   5
"""


def binary_search_iter(array, x):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -777


def binary_search_recur(array, x, low, high):

    if high >= low:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search_recur(array, x, low, mid-1)

        else:
            return binary_search_recur(array, x, mid + 1, high)

    else:
        return -777


# data = sorted([-100, 5, 1, 12, 0, 6.7]) # <- ТОЛЬКО С ОТСОРТИРОВАННЫМИ ПОСЛЕДОВАТЕЛЬНОСТЯМИ
#
# print(data)
# result = binary_search_recur(data, 0, 0, len(data) - 1)
# print(result)








