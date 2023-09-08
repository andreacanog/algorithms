import re
StrRates = "5.0, 100, 5.5, 101, 6.0, 102:L10, 5.0, 99, 5.5, 100, 6.0, 101:L20"
locks = "".join(re.findall("[L]\d+", StrRates)).split("L")

rates = sorted(set(re.findall("\d+[.]\d+", StrRates)), key=float)

str_trimmed = ",".join(StrRates.replace(":", ",").split(", ")).split(",")

prices = []

for x, price in enumerate(str_trimmed):
    if price.isdigit():
        prices.append(price)

matrix = [locks]

for i in range(len(locks)):

    row = ["" for _ in range(len(locks))]
    row[0] = rates[i]
    matrix.append(row)

for i in range(1, len(matrix)):
    idx = i - 1
    for j in range(1, len(matrix[i])):
        matrix[i][j] = prices[idx]
        idx += len(rates)
for x in range(len(matrix)):
    print(matrix[x])



    