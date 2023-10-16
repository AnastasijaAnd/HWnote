from note_v import *


def write_name(name):
    with open("note.csv", "a", encoding="UTF-8") as file:
        file.write(name)

def search_smth_in_note():
    search_option = int(input('Выберите вариант поиска: \n 1 - id \n 2 - название \n 3 - дата и время \n'))
    look_world = input("Введите слово поиска:\n") 
    with open("note.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        fnd_lst = []
        if search_option == 1 :
            for row in lst:
                if row.split(',')[0] == look_world:
                    fnd_lst.append(row)
        if search_option == 2:
            for row in lst:
                if row.split(',')[1] == look_world:
                    fnd_lst.append(row)
        if search_option == 3:
            for row in lst:
                if row.split(',')[2] == look_world:
                    fnd_lst.append(row)
        return fnd_lst
 

def change_smth_in_note():
    with open("note.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print("Что нужно изменить?:")
        print(*search_smth_in_note())
        id = input('Введите id заметки: ')
        print('Введите новые данные: ')
        for i in range(len(lst)):
            if lst[i].split(',')[0] == id:
                lst[i] = id + "," + change_note_name()  
    with open("note.csv", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)

def delete_smth_in_note():
    with open("note.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print("Вы хотите удалить?:")
        print(*search_smth_in_note())
        id = input('Введите id заметки: ')
        for i in range(len(lst)):
            if lst[i].split(',')[0] == id:
                lst[i] =''
    with open("note.csv", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)

def all_note():
     with open("note.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            print(row)
