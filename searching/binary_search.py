array = list(map(int, input().split()))
find = int(input())


def binary_search(array, low, high):
    if low < high:
        mid = (low + high) // 2
        if find < array[mid]:
            return binary_search(array, low, mid)
        elif find > array[mid]:
            return binary_search(array, mid+1, high)
        else:
            return mid
    return -1


index = binary_search(array, 0, len(array))
print(index)
