def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    mergeTwoSortedList(left, right, arr)




def mergeTwoSortedList(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            arr[k] = a[i]
            k += 1
            i += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    # a = [5,8,12,56]
    # b = [7,9,45,51]
    arr  = [10,3,15,7,8,23,98,29]
    # print(mergeTwoSortedList(a,b))
    merge_sort(arr)
    print(arr)
