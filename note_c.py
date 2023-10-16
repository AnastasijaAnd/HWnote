from note_v import *
from note_db import *


def main():
    while True:
        num = input_number()
        if num == 1:
            res = add_name_note()
            write_name(res)
            print('Успешно записано\n')
        if num == 2:
            print('Все заметки:\n')
            all_note()    
        if num == 3:
            print(*search_smth_in_note(), sep= "; ")
            print('Поиск закончен\n')
        if num == 4:
            change_smth_in_note()
            print('Успешно изменено\n')
        if num == 5:
            delete_smth_in_note()
            print('Успешно удалено\n')
        if num == 7:
            with open("note.csv", "w", encoding="UTF-8") as file:
                file.write('')
            print('Все заметки удалены успешно\n')
        if num == 0:
            break

main()