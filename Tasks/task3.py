#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    a = tuple(map(int, input().split()))
    if len(a) < 2:
        print("Кортеж должен содержать хотя бы 2 элемента", file=sys.stderr)
        exit(1)

    last_pos = 0

    for i, (x, y) in enumerate(zip(a, a[1:])):
        if x % 2 == 0 and y % 2 == 0:
            last_pos = i

    if last_pos == 0:
        print("В кортеже нет пар соседних четных элементов")
    else:
        print("Элементы перед последней парой четных:")
        for elem in a[:last_pos]:
            print(elem, end=" ")