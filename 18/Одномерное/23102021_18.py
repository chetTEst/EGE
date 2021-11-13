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

