#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    A = tuple(map(int, input().split()))
    if len(A) < 2:
        print("Кортеж должен содержать хотя бы 2 элемента", file=sys.stderr)
        exit(1)

    found_pair = False
    last_pos = -1

    for i in range(len(A) - 1):
        if A[i] % 2 == 0 and A[i + 1] % 2 == 0:
            found_pair = True
            last_pos = i

    if found_pair:
        print("Элементы перед последней парой четных:")
        for i in range(last_pos):
            print(A[i], end=" ")
    else:
        print("В кортеже нет пар соседних четных элементов")