# Enter numbers space separated
array = list(map(int, input().split()))


def selection_sort(array):
    for i in range(len(array)):
        __min__ = i
        for j in range(i+1, len(array)):
            if array[j] < array[__min__]:
                __min__ = j
        if __min__ != i:
            array[i], array[__min__] = array[__min__], array[i]
    return array


print(selection_sort(array))
