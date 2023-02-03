# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
n = int(input("Введите шестизначное число: "))

sumFirst=0
i=1
while i<=3:
    sumFirst=sumFirst+int(float(n%10))
    n=n/10
    i=i+1
print(sumFirst)

sumSecond=0

while i<=6:
    sumSecond=sumSecond+int(float(n%10))
    n=n/10
    i=i+1
print(sumSecond)

if (sumFirst==sumSecond):
    print ('Это счастливый билет')
else:
    print ('Это не счастливый билет')
