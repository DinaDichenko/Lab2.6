#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys

if __name__ == '__main__':
    poezd = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название пункта назначения? ")
            no = input("Номер поезда? ")
            time_str = input("Введите время отправления (чч:мм:)\n")
            t =  datetime.datetime.strptime(time_str, '%H:%M').time()

            # Создать словарь.
            po = {
                'name': name,
                'no': no,
                't': t,
            }

            # Добавить словарь в список.
            poezd.append(po)
            # Отсортировать список в случае необходимости.
            if len(po) > 1:
                poezd.sort(key=lambda item: item.get('no', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 10,
                '-' * 20,
                '-' * 8,
            )
            print(line)
            print(
                '| {:^10} | {:^20} | {:^8} |'.format(
                    " No ",
                    "Название",
                    "Время"
                )
            )
            print(line)

            for idx, po in enumerate(poezd, 1):
                print(
                    '| {:>10} | {:<20} | {''} |'.format(
                        po.get('no', ''),
                        po.get('name', ''),
                        po['t']
                    )
                )
            print(line)

        elif command == ('select'):
            count = 0
            nom = input("Введите номер поезда: ")
            for idx, po in enumerate(poezd, 1):
                if po['no'] == str(nom):
                    print("Название пункта: ", po['name'], "\nВремя отправления: ", po['t'])
                    count += 1

            if count == 0:
                print("Поезда с таким номером нет")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер> - запросить поезд по номеру;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
