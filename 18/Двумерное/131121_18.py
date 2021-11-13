'''
Исходные данные записаны в файле 18-6.xls в виде электронной таблицы прямоугольной формы. Робот может двигаться только вниз или вправо. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой верхней клетки в правую нижнюю. В ответе укажите два числа – сначала максимальную сумму, затем минимальную.
'''

f = open("18-6.csv")
data = [d.strip().split(';') for d in f.readlines()]
answer = [[""]*len(data[0]) for _ in range(len(data))]
answer[0][0] = int(data[0][0])

for i in range(1, len(data[0])):
    answer[0][i] = answer[0][i-1] + int(data[0][i])
for i in range(1, len(data)):
    answer[i][0] = answer[i-1][0] + int(data[i][0])

for x in range(1, len(data[0])):
    for y in range(1, len(data)):
        answer[y][x] = max(answer[y-1][x]+int(data[y][x]), answer[y][x-1]+int(data[y][x]))

print(answer[-1][-1])