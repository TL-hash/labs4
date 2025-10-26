#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    p = math.prod([item for item in A if item < 0])
    print(p)