def bubble_sort(array):
    for i in range(len(array)):

    # loop to compare array elements
        for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
            if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
                array[j], array[j+1] = array[j+1],array[j]
                # temp = array[j]
                # array[j] = array[j+1]
                # array[j+1] = temp



arr = [-2, 45, 0, 11, -9]
bubble_sort(arr)
print(arr)