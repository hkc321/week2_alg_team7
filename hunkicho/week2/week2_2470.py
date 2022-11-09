# https://www.acmicpc.net/problem/2470

import sys
import itertools

count = list(map(int, sys.stdin.readline().split()))
lists =  list(map(int, sys.stdin.readline().split()))

comb = list(itertools.combinations(lists,2))
hap = 2000000000

for i in comb:
    print(sum(i))
    if abs(0 - sum(i)) < hap:
        print_list = i

print(print_list[0], print_list[1])