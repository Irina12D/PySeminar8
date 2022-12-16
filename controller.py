import view
import phonebook as pb
import Data_Base as db

can_work = False


def main_manu(selection: int):
    match selection:
        case 1:
            global can_work
            can_work = db.laod_db()
            view.load_succsess(can_work)
        case 2:
            phonebook = pb.get_phonebook()
            view.print_phonebook(phonebook)
        case 3:
            if can_work:
                newcontact = view.new_contact()
                pb.add_contact(newcontact)
                db.save_db()
                view.add_succsess()
            else:
                view.print_cant_work()
        case 4:
            if can_work:
                view.select_a_number()
                phonebook = pb.get_phonebook()
                view.print_phonebook(phonebook, 6)
                id = view.change_contact(len(phonebook), 4)
                selected_contact = view.new_contact(4)
                result = pb.edit_contact(id - 1, selected_contact)
                if result:
                    db.save_db()
                view.edit_succsess(result)
            else:
                view.print_cant_work()
        case 5:
            if can_work:
                view.select_a_number()
                phonebook = pb.get_phonebook()
                view.print_phonebook(phonebook, 5)
                id = view.change_contact(len(phonebook), 5)
                result = pb.remove_contact(id - 1)
                if result:
                    db.save_db()
                view.delet_succsess(result)
            else:
                view.print_cant_work()
        case 6:
            if can_work:
                search_data = view.find_contact()
                view.search_result(pb.find_contacts(search_data))
            else:
                view.print_cant_work()
        case 0:
            return True


def start():
    while True:
        selection = view.menu()
        if main_manu(selection):
            view.print_the_end()
            break


