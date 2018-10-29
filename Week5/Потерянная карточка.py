# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.

n = int(input())
sumNFull = 0
sumN = 0

for i in range(1, n+1):
    if i != n:
        x = int(input())
        sumN += x
    sumNFull += i

z = sumNFull - sumN
print(z)
