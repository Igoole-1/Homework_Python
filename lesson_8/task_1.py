# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 5. Добавить контакт
# Чтение, поиск, добавить контакт, сохранить
dataPath = r'C:\Users\igool\OneDrive\Рабочий стол\python\semi_8\contacts.txt'

def output(dataPath):
    with open(dataPath, 'r', encoding="utf-8") as f:
        print(f.read())


def add_contact(dataPath):
    new_contact = input('Введите новый контакт - ФИО телефон: ')
    with open(dataPath, 'a', encoding="utf-8") as f:
        f.write(f'\n{new_contact}')
    print('Новый контак добавлен')

        
def search(dataPath):
    with open(dataPath, 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию: ')
        for line in f:
            if X in line:
                print(line)


def change_contact(dataPath):
    with open(dataPath, 'r+', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для изменения: ')
        Y = input('Введите на что изменить: ')
        old_data = f.read()
        new_data = old_data.replace(X, Y)
        with open(dataPath, 'w', encoding="utf-8") as f:
            f.write(new_data)

def remove_contact(dataPath):
    with open(dataPath, 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open(dataPath, 'w', encoding="utf-8") as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)

   

def action():
    print("Меню справочника: \nЦифра 1 - покажет весь справочник  \nЦифра 2 - для добавления нового контакта \nЦифра 3 - поможет найти контакт в справочнике \nЦифра 4 - для изменения контакта \nЦифра 5 - для удаления контакта")
    while (input1:= int(input('Выберите действие 1, 2, 3, 4, 5. \nДля выхода из меню нажмите 0 ')))!= 0:
        if input1 == 1:
            output(dataPath)
        if input1 == 2:
            add_contact(dataPath)
        if input1 == 3:
            search(dataPath)
        if input1 == 4:
            change_contact(dataPath)
        if input1 == 5:
            remove_contact(dataPath)
        

action()

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных