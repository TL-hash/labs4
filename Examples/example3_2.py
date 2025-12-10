#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    a = tuple(map(int, input().split()))
    if len(a) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    s = sum(elem for elem in a if abs(elem) < 5)
    print(s)