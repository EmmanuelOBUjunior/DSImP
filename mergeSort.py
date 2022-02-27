def mergeTwoSortedList(a, b):
    sortedList = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sortedList.append(a[i])
            i += 1
        else:
            sortedList.append(b[j])
            j += 1

    return sortedList


if __name__ == '__main__':
    a = [5,8,12,56]
    b = [7,9,45,51]

    print(mergeTwoSortedList(a,b))
