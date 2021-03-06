def shellSort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2





if __name__ == '__main__':
    elements = [21,38,29,17,4,24,11,32,9]
    shellSort(elements)
    print(elements)