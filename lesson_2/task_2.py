# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3
S = int(input("Введите сумму двух чисел: "))
P = int(input("Введите произведение двух чисел: "))
i=1
while i<=int(S//2):
    if i*(S-i)==P:
        print(i)
        print(S-i)
    i=i+1