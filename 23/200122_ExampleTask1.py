"""
У исполнителя Калькулятор две команды, которым присвоены номера:
1. прибавь 2
2. умножь на 2
Сколько есть программ, которые число 2 преобразуют в число 40?
"""

def F(start, n):
    if start == n:
        return 1
    if n%2 == 0:
        return F(start, n-2) + F(start, n/2)
    else:
        return 0

print(F(2,40))