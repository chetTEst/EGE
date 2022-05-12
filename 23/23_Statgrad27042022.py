def F(n, s):
    if n < s:
        return 0
    if n == s:
        return 1
    if n%10 == 1 and n > 10:
        return F(n-1, s)+F((n-1)//10, s)
    return F(n-1, s)

print(F(333, 1))