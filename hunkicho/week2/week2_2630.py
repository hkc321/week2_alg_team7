# https://www.acmicpc.net/problem/2630

import sys

length = int(sys.stdin.readline())
arr = [[0]*length for i in range(length - 1)]

for i in range(length):
    arr[i] = list(map(int, sys.stdin.readline().split()))



