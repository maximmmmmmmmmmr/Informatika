# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"   # имя фаила откуда читаем
OUTPUT_FILENAME = "output.json"   # куда записываем

def task() -> None:
    # TODO считать содержимое csv файла
    file_csv = open(INPUT_FILENAME, 'r')
    vse_stroki = file_csv.readlines()  # читаю все строчки

    zagolovki = vse_stroki[0].strip().split(',')  # первая строчка - это названия столбцов

    resultat = []
    for i in range(1, len(vse_stroki)):

        tek_stroka = vse_stroki[i]
        tek_stroka = tek_stroka.strip()   # удаляю лишние пробелы и переносы в конце
        znacheniya = tek_stroka.split(',') # разбиваю строчку по запятым
        slovar = {}


        for j in range(len(zagolovki)):

            if j < len(znacheniya):
                slovar[zagolovki[j]] = znacheniya[j]
            else:
                slovar[zagolovki[j]] = '' # если значений больше чем заголовков ставлю пустую строчку
        resultat += [slovar]    # добавляю словарь в список результатов

    file_json = open(OUTPUT_FILENAME, 'w')     # открываю фаил на запись


    json_stroka = json.dumps(resultat, indent=4)  # преобразую список словарей в джсон строку с отступами 4
    file_json.write(json_stroka) # записываю в фаил

if __name__ == '__main__':
    task()
    file_itog = open(OUTPUT_FILENAME, 'r')
    for stroka in file_itog:
        print(stroka, end='')
