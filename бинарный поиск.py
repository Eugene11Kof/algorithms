from random import randint, choice
# A = [randint(1,99) for i in range(10)]
A = [3, 5, 6, 66, 69, 82, 90, 93, 94, 96]
A.sort()
print(A)
key = choice(A)
print(key)
left = -1
right = len(A) 
while right > left + 1: 
    middle = (left + right) // 2 
    if A[middle] > key: 
        right = middle 
    else: 
        left = middle
print(left)

