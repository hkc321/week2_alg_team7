# https://www.acmicpc.net/problem/18258

import sys

count = int(sys.stdin.readline())
q = [None] * 2000001
print_list = []
front = 0
back = 0
no = 0

for i in range(count):
    command = str(sys.stdin.readline().rstrip())

    if command[-1].isdecimal():
        q[back] = command.split()[1]
        back += 1
        no += 1

    if command == "pop":
        if no > 0:
            print_list.append(q[front])
            front += 1
            no -= 1
        else:
            print_list.append(-1)

    if command == "size":
        print_list.append(no)

    if command == "empty":
        if no > 0:
            print_list.append(0)
        else:
            print_list.append(1)

    if command == "front":
        if no > 0:
            print_list.append(q[front])
        else:
            print_list.append(-1)
    
    if command == "back":
        if no > 0:
            print_list.append(q[back - 1])
        else:
            print_list.append(-1)

for j in print_list:
    print(j)

