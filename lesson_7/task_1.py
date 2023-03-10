# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# 
# Фразы отделяются друг от друга пробелами. 

# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 

# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод:
# Парам пам-пам

def rhythm(a,b):
    count = [(sum(map(lambda item, sum = 0: sum +1 if item in b else sum, i))) for i in a]
    return count 

poem = str(input("Введите Ваше стихотворение: "))
phrases = poem.split(' ')
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
print(rhythm(phrases,vowels))

if len(set(rhythm(phrases,vowels)))==1:
    print("Парам пам-пам")
else:
    print("Пам парам")








# song = input()
# volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
# parts = song.split()
# itog = list()

# def win_and_pooh(song):
#     volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
#     parts = song.split()
#     itog = list()
#     for item in parts:
#         k = 0
#         for letter in item:
#             if letter in volwes:
#                 k += 1
#         itog.append(k)
#     if len(set(itog)) == 1:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')