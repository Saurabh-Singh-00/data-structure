# Enter numbers space separated
array = list(map(int, input().split()))


def merge(left_array, right_array):
    i, j = 0, 0
    res_array = []
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            res_array.append(left_array[i])
            i += 1
        else:
            res_array.append(right_array[j])
            j += 1
    while i < len(left_array):
        res_array.append(left_array[i])
        i += 1
    while j < len(right_array):
        res_array.append(right_array[j])
        j += 1
    return res_array


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left_array = merge_sort(array[0:mid])
    right_array = merge_sort(array[mid:len(array)])
    print(left_array, right_array)
    return merge(left_array, right_array)


print(merge_sort(array))
