def menu():
    print('\n1. Загрузить телефонный справочник'\
          '\n2. Отобразить телефонный справочник'\
          '\n3. Добавить контакт'\
          '\n4. Изменить контакт'\
          '\n5. Удалить контакт'\
          '\n6. Найти контакт'\
          '\n0. Выход\n')
    return menu_selection()


def menu_selection():
    while True:
        try:
            selection = int(input("Выберите пункт меню: "))
            if 0 <= selection <= 7:
                return selection
            else:
                print("Неверный пункт меню!")
        except:
            print("Неверный пункт меню!")


def load_succsess(exist):
    if not exist:
        print('На диске отсутствует файл справочника')
    else:
        print('Телефонный справочник загружен')


def print_cant_work():
    print('Телефонный справочник отсутствует. Требуется загрузить его!')


def print_phonebook(phonebook: list, type = 2):
    if not phonebook:
        print_cant_work()
    else:
        for id, item in enumerate(phonebook, 1):
            print(id, *item)
        if type == 2:
            input("\nнажмите клавишу Enter для продолжения... ")
        else:
            print()


def add_succsess():
    print('\nНовый контакт успешно добавлен')


def new_contact(type = 3):
    input_invite = ['Введите имя контакта: ',
                    'Введите номер телефона: ',
                    'Введите комментарий: ']
    if type == 4:
        print("Внимание! Все изменения сразу сохраняются в справочнике!")
        input_invite = ['Измените имя контакта (Enter - оставить без изменения): ',
                        'Измените номер телефона (Enter - оставить без изменения): ',
                        'Измените комментарий (Enter - оставить без изменения): ']
    if type == 6:
        input_invite = ['Введите имя контакта или нажмите Enter, чтобы пропустить: ',
                        'Введите номер телефона или нажмите Enter, чтобы пропустить: ',
                        'Введите комментарий или нажмите Enter, чтобы пропустить: ']
    name = input(input_invite[0])
    phone = input(input_invite[1])
    comment = input(input_invite[2])
    return [name, phone, comment]

def select_a_number():
    print('\nВыберите номер контакта из телефонной книги:')


def change_contact(length: int, type: int):
    if type == 5:
        word = 'удаляемого'
    elif type == 4:
        word = 'изменяемого'
    while True:
        try:
            id = int(input(f"Укажите номер {word} контакта: "))
            if 1 <= id <= length:
                return id
            else:
                print("Нет такого номера в справочнике!")
        except:
            print("Неверно! Введите номер из списка!")


def confirmation_of_deletion(name):
    confirmation = input(f"Вы действительно хотите удалить контакт {name}? Y / N: ")
    if confirmation.upper() == 'Y' or confirmation.upper() == 'Н':
        return True
    return False


def edit_succsess(result_action):
    if result_action:
        print('\nДанные выбранного контакта изменены')
    else:
        print('\nКонтакт остаётся в справочнике с первоначальными данными')


def delet_succsess(confirmation):
    if confirmation:
        print("\nКонтакт успешно забыт и ушёл из вашей жизни навечно")
    else:
        print("\nВовремя одумались, контакт остаётся с нами")


def find_contact():
    print("Введите данные для поиска")
    print("Вы можете ввести только имя контакта, только номер телефона или только комментарий к контакту")
    print("Или же можно ввести несколько параметров контакта для более результативного поиска")
    return new_contact(6)


def search_result(result):
    if result:
        print("\nРезультаты поиска:")
        for item in result:
            print(*item)
    else:
        print("\nПо вашему запросу ничего не найдено")


def print_the_end():
    print("\nДо свидания, до новых встреч!")