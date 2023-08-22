arr = [12,22,34,52,1,77]


def linear_search(a, x):
    for i,j in enumerate(a):
        if j == x:
            print(i)
            print('got it')
        else:
            print("Not Found")

linear_search(arr, 34)            

