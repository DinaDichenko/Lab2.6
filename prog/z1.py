#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    school = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Класс? ")
            year = int(input("Количество учеников? "))

            schooler = {
            'name': name,
            'year': year,
            }
            school.append(schooler)
            if len(school) > 1:
                school.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} |'.format(
                    "No",
                    "Класс",
                    "Количество учеников"
                )
            )
            print(line)

            for idx, schooler in enumerate(school, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} |'.format(
                        idx,
                        schooler.get('name', ''),
                        schooler.get('year', 0)
                    )
                )
            print(line)

        elif command == 'del':
            d = input("Какой класс расформирован? ")
            for idx, schooler in enumerate(school, 1):
                if schooler['name'] == d:
                    del school[idx - 1]

        elif command == 'edit':
            ed = input("В каком классе изменилось количество учеников? ")
            col = input("Сколько учеников стало? ")
            for idx, schooler in enumerate(school, 1):
                if schooler['name'] == ed:
                    schooler['year'] = col
        elif command == 'sum':
            s = 0
            for idx, schooler in enumerate(school, 1):
                s += int(schooler['year'])
            print("Количество учеников в школе: ", s)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить класс;")
            print("list - вывести список классов;")
            print("sum - общее количество учеников в школе")
            print("del - расформировать класс")
            print("edit - изменить количество учеников в классе")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)