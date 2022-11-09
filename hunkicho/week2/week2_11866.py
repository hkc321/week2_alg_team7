# https://www.acmicpc.net/problem/11866

import sys

n,k = list(map(int,sys.stdin.readline().split()))
no = n
front = k
back = k
print_list = "<"

circle = [None] * n

for i in range(n):
    circle[i] = i + 1

while no > 0:
    print("front",front)
    if front >= n:
        front = 0 + (front - n)
    print_list += str(circle[front - 1]) + ", "
    no -= 1
    front += k

print(print_list[:-2] + ">")