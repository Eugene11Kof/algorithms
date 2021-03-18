from random import randint
n = 20
a = [randint(1, 99) for i in range(n)]
print(a)
for j in range(n-1):
    for i in range(n-j-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(a)
