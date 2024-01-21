main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

main_menu_choise = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно загружена'

save_successful = 'Телефонная книга успешно сохранена'

empty_phone_book = 'Телефонная книга пуста или не открыта!'

new_contact = ['Введите ФИО: ',
               'Введите номер телефона: ',
               'Введите коментарий: ']


def new_contact_add_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен.'


input_search_word = 'Введите текст для поиска: '


def contacts_not_found(word: str) -> str:
    return f'Контакты содержащие {word} не найдены!'


input_id_change_contact = 'Введите ID контакта, который хотите изменить: '

change_contact = ['Введите новое ФИО или ENTER, если хотите оставить без изменений: ',
                  'Введите новый номер телефона или ENTER, если хотите оставить без изменений: ',
                  'Введите новый коментарий ФИО или ENTER, если хотите оставить без изменений: ']


def contact_change_successfil(name: str) -> str:
    return f'Контакт {name} успешно изменен.'


input_id_delete_contact = 'Введите ID контакта, который хотите изменить: '


def contact_delete_successfil(name: str) -> str:
    return f'Контакт {name} успешно удален.'


good_bay = 'До новых встреч!'
