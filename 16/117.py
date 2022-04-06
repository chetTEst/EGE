def F(n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 1:
        return 1 + F(n-1)
    else:
        return F(n/2)


for n in range(1, 200):
    print(n, F(n))