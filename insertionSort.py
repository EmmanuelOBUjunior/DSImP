def insertionSort(elements):
    size = len(elements)
    for i in range(1, size):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor


if __name__ == '__main__':
    elements = [11,8,20,6,2,16,25]

    insertionSort(elements)
    print(elements)