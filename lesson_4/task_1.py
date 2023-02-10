# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
N = int(input("Введите количество элементов в первом массиве: "))
M = int(input("Введите количество элементов во втором массиве: "))
A = []
for item in range(N):
    user_num = int(input("Введите число: "))
    A.append(user_num)
print(A)
B = []
for item in range(M):
    user_num = int(input("Введите число: "))
    B.append(user_num)
print(B)
unique_one = set(A)
unique_two = set(B)
# print(unique_one)
# print(unique_two)
unique_numbers = unique_one.intersection(unique_two)
print(*sorted(unique_numbers))