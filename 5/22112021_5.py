"""
Автомат обрабатывает натуральное число N > 1 по следующему алгоритму:
1. Строится двоичная запись числа N.
2. В конец записи (справа) дописывается вторая справа цифра двоичной записи.
3. В конец записи (справа) дописывается вторая слева цифра двоичной записи.
4. Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом:
1. Двоичная запись числа N: 1011.
2. Вторая справа цифра 1, новая запись 10111.
3. Вторая слева цифра 0, новая запись 101110.
4. Результат работы алгоритма R = 46.
Для скольких значений N в результате работы алгоритма получится число, принадлежащее отрезку [150; 200]?
"""

def avto(n):
    n = bin(n)[2:]
    return int(n + n[-2] + n[1], 2)
c = 0
for i in range(30, 1000):
    if 150<=avto(i)<=200:
        c += 1
print(c)
