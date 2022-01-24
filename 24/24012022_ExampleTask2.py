"""
В текстовом файле k7b-4.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите максимальную длину цепочки вида EBCFEBCFEBCF.... (состоящей из фрагментов EBCF, последний фрагмент может быть неполным).
"""

with open("k7b-4.txt") as f:
    data = f.read()

s1 = "EBCF"
C = []
m = 0
for i in data:
    if i == s1[m%4]:
        m += 1
    else:
        C.append(m)
        m = 0
print(max(C))