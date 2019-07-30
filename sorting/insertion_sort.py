# Enter numbers space separated
array = list(map(int, input().split()))


def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        insert_at = -1
        already_sorted = i - 1
        for j in range(already_sorted, -1, -1):
            if array[j] > current:
                array[j+1] = array[j]
            else:
                insert_at = j
                break
        array[insert_at+1] = current
    return array


print(insertion_sort(array))
