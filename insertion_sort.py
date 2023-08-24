def insertionSort(array):
    for step in range(1, len(array)):
        item = array[step]
        j = step - 1

        while(j >= 0 and item < array[j]):
            array[j+1] = array[j]
            j = j -1

        array[j+1] = item

data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)