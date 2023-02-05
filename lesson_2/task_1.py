# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
n = int(input("Введите количество монеток: "))
money = []
for i in range(n):
    user_money = int(input("Введите 1 для орла, 0 для решки: "))
    money.append(user_money)
print(money)

countOne=0
countTwo=0
for i in range(n):
    if (money[i]==0):
        countOne+=1
    else:
        countTwo+=1
    #     # i+=1
print(countOne)
print(countTwo)
if countOne<countTwo:
    print (countOne)
else:
    print(countTwo)