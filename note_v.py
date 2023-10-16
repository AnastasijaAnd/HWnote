from note_db import *
from datetime import datetime
from datetime import date

def input_number():
    answer= int(input("Выберете действие:\n1-записать новую заметку\n2-показать все заметки\n3-найти\n4-изменить\n5-удалить\n6-отсортировать\n7-очистить все\n0-закончить работу\n"))
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
    nnote = input('Введите заметку: ')
    cr_date = date.today().strftime("%d-%m-%Y")
    cr_time = datetime.now().time().strftime("%H:%M:%S")
    res = id + "," + name + "," + nnote + ',' + cr_date + ',' + cr_time +'\n' 
    return res

def change_note_name():
    name = input('Введите название: ')
    nnote = input('Введите заметку: ')
    cr_date = date.today().strftime("%Y-%m-%d")
    cr_time = datetime.now().time().strftime("%H:%M:%S")
    res =name + "," + nnote + ',' + cr_date + ',' + cr_time + '\n' 
    return res
