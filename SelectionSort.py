def selection_Sort(elements):
    size = len(elements)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j

        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]



if __name__ == '__main__':
    test = [
        [234,12,15,8,61,53,23,27],
        [89,78,61,53,23,21,17,12,9,7,6,2,1],
        [],
        [1,5,8,9],
        [5]
    ]

    for element in test:
        selection_Sort(element)
        print(element)