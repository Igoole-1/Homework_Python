# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
N = int(input("Введите трехзначное число: "))
print(N)
sum=0
while N>0:
    sum+=N%10
    N=N//10
print(sum)