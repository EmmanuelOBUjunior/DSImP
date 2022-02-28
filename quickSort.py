def swap(a, b, arr):
    if a!=b:
        arr[a], arr[b] = arr[b], arr[a]



def partition(arr, start, end):
    pivotI = start
    pivot = arr[pivotI]


    while start < end:
        while start < len(arr) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivotI, end, elements)

    return end


def quickSort(arr, start, end):
    if start < end:
        partI =  partition(arr, start, end)
        quickSort(elements, start, partI - 1)
        quickSort(elements, partI + 1, end)





if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quickSort(elements, 0, len(elements) - 1)
    print(elements)