"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [5408238; 5408389], простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку.
"""

for i in range(540823999577777, 5408389099577777, 2):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i)