from note_db import *
from datetime import datetime
from datetime import date

def input_number():
    answer= int(input("Выберете действие:\n1-записать новую заметку\n2-показать все заметки\n3-найти\n4-изменить\n5-удалить\n6-отсортировать\n0-закончить работу\n"))
    return answer

def add_name_note():
    id = '1'
    with open("note.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.sort(key= lambda x: int(x.split(',')[0]))
        for row in lst:
            if row.split(',')[0] == id:
                id = str(int(id) + 1) 
    name = input('Введите название: ')
    nnote = input('Ввелите заметку: ')
    cr_date = date.today().strftime("%Y-%m-%d")
    cr_time = datetime.now().time().strftime("%H:%M:%S")
    res = id + "," + name + "," + nnote + ',' + cr_date + ',' + cr_time +'\n' 
    return res

def input_search_option():
    search_option = int(input('Выберите вариант поиска: \n 1 - id \n 2 - название \n 3 - дата и время \n'))
    return search_option

def input_want_to_find():
    char = input("Введите слово поиска:\n")
    return char

def change_name_note():
    name = input('Введите имя: ')
    nnote = input('Ввелите фамилию: ')
    cr_date = date.today().strftime("%Y-%m-%d")
    cr_time = datetime.now().time().strftime("%H:%M:%S")
    res =name + "," + nnote + ',' + cr_date + ',' + cr_time + '\n' 
    return res

def input_sort_option():
    sort_option = int(input('Выберите вариант сортировки: \n 1 - id \n 2 - название \n 3 - дата и время \n'))
    return sort_option