# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8 
N = int(input("Введите число: "))
count = 1
# print(count)
while count < N:
    if count <=N:
        print(count)
        count = count*2
    
# for i in range(N):  
#     print(count)  
#     count = count*2
#     if count>N:
#         break         