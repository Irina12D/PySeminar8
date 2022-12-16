import os
import phonebook

db_path = 'telephone_directory.txt'

def create_list(data: list):
    phonebook = []
    for item in data:
        phonebook.append(item.strip().split(';'))
    return phonebook

def laod_db():
    if not os.path.exists(db_path):
        return False
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    phonebook.set_phonebook(create_list(data))
    return True

def create_data():
    pb = phonebook.get_phonebook()
    data = []
    for contact in pb:
        data.append(';'.join(contact) + '\n')
    data[-1] = data[-1][:-1]
    return ''.join(data)

def save_db():
    with open(db_path, 'w', encoding='UTF-8') as file:
        file.write(create_data())
