import json


def show_contacts():
    with open('contacts.txt', 'r', encoding='UTF-8') as file:
        data = file
        for line in data:
            print(*list(line.split(' ')))


def add_contacts():
    cont = input('Введите ФИО и номер телефона через пробел: ')
    with open('contacts.txt', 'a', encoding='UTF-8') as file:
        file.write(cont + '\n')
        print('\n Контакт добавлен.\n')


def search():
    inp = input('Для поиска введите имя или фамилию: ')
    with open('contacts.txt', 'r', encoding='UTF-8') as file:
        data = file
        for line in data:
            if inp in list(line.split(' ')):
                print('\nРезультат поиска\n', *list(line.split(' ')))


def edit_contact():
    pass


# def delete_contact():
#     with open('contacts.txt', 'r+', encoding='UTF-8') as file:
#         data = file
#         for line in data:
#             print(*line.split(' '))
#         delete = input('Укажите фамилию для удаления контакта: ')
#         for line in data:
            # if delete in list(line.split(' ')):





while True:
    user_input = int(input('Меню:\n'
                           '1.Показать контакты\n'
                           '2.Добавить контакты\n'
                           '3.Поиск\n'
                           '4.Изменить контакт\n'
                           '5.Удалить контакт\n'
                           '0.Выход\n'
                           'Ввод: '))
    if user_input == 1:
        show_contacts()
    elif user_input == 2:
        add_contacts()
    elif user_input == 3:
        search()
    elif user_input == 4:
        edit_contact()
    elif user_input == 5:
        delete_contact()
    elif user_input == 0:
        break
    else:
        print('\nНекорректный ввод!\n')
