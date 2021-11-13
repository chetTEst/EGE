'''
Дана последовательность вещественных чисел. Из неё необходимо выбрать несколько подряд идущих чисел так, чтобы каждое следующее число было больше предыдущего. Какую максимальную сумму могут иметь выбранные числа? В ответе запишите целую часть полученной суммы. Исходные данные записаны в виде столбца электронной таблицы в файле 18-18.xls.
'''

f = open('18-18.csv')
data = f.readlines()
summ = float(data[0])
maxSum = float(data[0])
for i in range(1, len(data)):
    if float(data[i]) > float(data[i-1]):
        summ += float(data[i])
    else:
        summ = float(data[i]) #0
    if summ > maxSum:
        maxSum = summ
print(maxSum)

