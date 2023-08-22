n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        count = count + 1
    
    # print(i)
print(count)

# Time complexity O(n**2)