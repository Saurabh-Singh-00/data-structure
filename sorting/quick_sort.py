# Enter numbers space separated
array = list(map(int, input().split()))


def partition(array, start=0, end=0) -> int:
    x = start
    pivot = array[start]
    for i in range(start+1, len(array)):
        if pivot > array[i]:
            x += 1
            array[x], array[i] = array[i], array[x]
    array[start], array[x] = array[x], array[start]
    return x


def quick_sort(array, left=0, right=0):
    if left >= right:
        return
    pivot_point: int = partition(array, start=left, end=right)
    quick_sort(array, left=left, right=pivot_point-1)
    quick_sort(array, left=pivot_point+1, right=right)
    return array


print(quick_sort(array, left=0, right=len(array)))
