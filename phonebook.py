import view
phonebook = []

def get_phonebook():
    global phonebook
    return phonebook


def set_phonebook(contact_list):
    global phonebook
    phonebook = contact_list


def add_contact(contact: list):
    global phonebook
    phonebook.append(contact)


def remove_contact(id: int):
    global phonebook
    expelled_name = phonebook[id][0]
    if view.confirmation_of_deletion(expelled_name):
        phonebook.pop(id)
        return True
    return False

def edit_contact(id: int, contact: list):
    global phonebook
    result = False
    for i in range(len(contact)):
        if contact[i] != '':
            phonebook[id][i] = contact[i]
            result = True
    return result

def find_contacts(contact_attributes: list):
    type_search = 0
    if contact_attributes[0] != '' and contact_attributes[1]!= '' and contact_attributes[2]!= '':
        type_search = 100   # поиск по всем трём параметрам (100% совпадение)
    elif contact_attributes[0] != '' and contact_attributes[1]!= '':
        type_search = 12   # поиск по имени и телефону (оба парамера должны совпадать, в конце списка будут контакты с одним из параметров)
    elif contact_attributes[0] != '' and contact_attributes[2]!= '':
        type_search = 13   # поиск по имени и комменту (оба парамера должны совпадать, в конце списка будут контакты с одним из параметров))
    elif contact_attributes[1] != '' and contact_attributes[2] != '':
        type_search = 23   # поиск по номеру телефона и комменту (оба парамера должны совпадать, в конце списка будут контакты с одним из параметров))
    elif contact_attributes[0] != '':
        type_search = 1    # поиск по имени (совпадение имени или фамилии)
    elif contact_attributes[1] != '':
        type_search = 2   # поиск по номеру телефона (точное совпадение номера)
    elif contact_attributes[2] != '':
        type_search = 3   # поиск комменту (совпадение на хотя бы одно слово из коммента)

    search_list = []
    global phonebook
    positon = 0
    match type_search:
        case 100:
            for item in phonebook:
                if contact_attributes == item:
                    search_list.append(item)
            if search_list:
                search_list.insert(positon, "Точное совпадение:")
                positon = len(search_list)
            or_2_parametrs = False
            for item in phonebook:
                if (
                        (contact_attributes[0].upper() in item[0].upper() and contact_attributes[2].upper() in item[2].upper()
                        or contact_attributes[0].upper() in item[0].upper() and contact_attributes[1] == item[1]
                        or contact_attributes[1] == item[1] and contact_attributes[2].upper() in item[2].upper())
                    and item not in search_list):
                    search_list.append(item)
                    or_2_parametrs = True
            if or_2_parametrs:
                search_list.insert(positon, "\nБолее релевантно запросу:")
                positon = len(search_list)
            or_name = False
            for item in phonebook:
                if contact_attributes[0].upper() in item[0].upper() and item not in search_list:
                    search_list.append(item)
                    or_name = True
            if or_name:
                search_list.insert(positon, "\nCовпадение по имени:")
                positon = len(search_list)
            or_number = False
            for item in phonebook:
                if contact_attributes[1] == item[1] and item not in search_list:
                    search_list.append(item)
                    or_number = True
            if or_number:
                search_list.insert(positon, "\nCовпадение по номеру:")
                positon = len(search_list)
            or_comment = False
            for item in phonebook:
                if contact_attributes[2].upper() in item[2].upper() and item not in search_list:
                    search_list.append(item)
                    or_comment = True
            if or_comment:
                search_list.insert(positon, "\nCовпадение по комментарию:")

        case 12:
            for item in phonebook:
                if contact_attributes[0].upper() in item[0].upper() and contact_attributes[1] == item[1]:
                    search_list.append(item)
            if search_list:
                search_list.insert(positon, "Точное совпадение:")
                positon = len(search_list)
            or_name = False
            for item in phonebook:
                if contact_attributes[0].upper() in item[0].upper() and item not in search_list:
                    search_list.append(item)
                    or_name = True
            if or_name:
                search_list.insert(positon, "\nCовпадение по имени:")
                positon = len(search_list)
            or_number = False
            for item in phonebook:
                if contact_attributes[1] == item[1] and item not in search_list:
                    search_list.append(item)
                    or_number = True
            if or_number:
                search_list.insert(positon, "\nCовпадение по номеру:")

        case 13:
            for item in phonebook:
                if contact_attributes[0].upper() in item[0].upper() and contact_attributes[2].upper() in item[2].upper():
                    search_list.append(item)
            if search_list:
                search_list.insert(positon, "Точное совпадение:")
                positon = len(search_list)
            or_name = False
            for item in phonebook:
                if contact_attributes[0].upper() in item[0].upper() and item not in search_list:
                    search_list.append(item)
                    or_name = True
            if or_name:
                search_list.insert(positon, "\nCовпадение по имени:")
                positon = len(search_list)
            or_comment = False
            for item in phonebook:
                if contact_attributes[2].upper() in item[2].upper() and item not in search_list:
                    search_list.append(item)
                    or_comment = True
            if or_comment:
                search_list.insert(positon, "\nCовпадение по комментарию:")

        case 23:
            for item in phonebook:
                if contact_attributes[1] == item[1] and contact_attributes[2].upper() in item[2].upper():
                    search_list.append(item)
            if search_list:
                search_list.insert(positon, "Точное совпадение:")
                positon = len(search_list)
            or_number = False
            for item in phonebook:
                if contact_attributes[1] == item[1] and item not in search_list:
                    search_list.append(item)
                    or_number = True
            if or_number:
                search_list.insert(positon, "\nCовпадение по номеру:")
                positon = len(search_list)
            or_comment = False
            for item in phonebook:
                if contact_attributes[2].upper() in item[2].upper() and item not in search_list:
                    search_list.append(item)
                    or_comment = True
            if or_comment:
                search_list.insert(positon, "\nCовпадение по комментарию:")

        case 1:
            for item in phonebook:
                if contact_attributes[0].upper() in item[0].upper():
                    search_list.append(item)

        case 2:
            for item in phonebook:
                if contact_attributes[1] == item[1]:
                    search_list.append(item)

        case 3:
            for item in phonebook:
                if contact_attributes[2].upper() in item[2].upper():
                    search_list.append(item)

    return search_list




