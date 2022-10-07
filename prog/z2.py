#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    slow = {
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four'
    }
    print("Словарь: ", slow)
    rev = {v: k for k, v in slow.items()}
    print("Обратный словарь", rev)
