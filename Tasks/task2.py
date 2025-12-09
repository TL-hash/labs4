#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    min_val = a[0]
    min_index = 0
    first_neg_index = 0
    second_neg_index = 0
    sum_between = 0

    for i, value in enumerate(a):
        if value < min_val:
            min_val = value
            min_index = i

        if value < 0:
            if first_neg_index == 0:
                first_neg_index = i
            elif second_neg_index == 0:
                second_neg_index = i

    print(f"Номер минимального элемента: {min_index}")

    if first_neg_index != 0 and second_neg_index != 0:
        sum_between = sum(a[first_neg_index + 1:second_neg_index])
        print(f"Сумма между первым и вторым отрицательными элементами: {sum_between}")
    else:
        print("Недостаточно отрицательных элементов для вычисления суммы")

    a.sort(key=lambda x: abs(x) > 1)

    print(f"Преобразованный список: {a}")