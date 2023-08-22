def binary_search(array, x, low, high):
    
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        elif(array[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [3, 4, 5, 6, 7, 8, 9]
x = 6
obj = binary_search(arr, x, 0, len(arr)-1)
if obj != -1:
    print(obj)
else:
    print('not found')
# print(obj)