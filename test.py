x = [5,1,4,2,7,3]
n = len(x)
def sorting(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if x[j] < x[min_idx]:
                min_idx = j

        if min_idx != i:
            x[i], x[min_idx] = x[min_idx], x[i]

sorting(x, n)
print(x)