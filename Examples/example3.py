#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    a = tuple(map(int, input().split()))
    if len(a) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    s = 0
    for item in a:
        if abs(item) < 5:
            s += item
            
    print(s)