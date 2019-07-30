# Enter numbers space separated
array = list(map(int, input().split()))


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


print(bubble_sort(array))
