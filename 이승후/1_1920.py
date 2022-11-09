import sys
from typing import Sequence


def binarySearch(a: Sequence, key: int):
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            print(1)
            return
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    print(0)


N = int(input())
A = sorted([int(i) for i in sys.stdin.readline().split()])
M = int(input())
Ms = [int(j) for j in sys.stdin.readline().split()]

for m in Ms:
    binarySearch(A, m)

