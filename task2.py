#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(float, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    i_min = a.index(min(a))
    print(f"Номер минимального элемента: {i_min}")

    i_neg = [i for i, item in enumerate(a) if item < 0]

    if len(i_neg) < 2:
        sum_between = 0
        print(f"Недостаточно отрицательных элементов для вычисления суммы")
    else:
        first_neg = i_neg[0]
        second_neg = i_neg[1]
        sum_between = sum(a[first_neg+1:second_neg])
        print(f"Сумма между первым и вторым отрицательными элементами: {sum_between}")

    low_abs = [item for item in a if abs(item) <= 1]
    high_abs = [item for item in a if abs(item) > 1]
    sorted_list = low_abs + high_abs
    #A.sort(key=lambda x: abs(x) > 1)

    print(f"Преобразованный список: {sorted_list}")
    #print(f"Преобразованный список: {A}")
