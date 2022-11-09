# https://www.acmicpc.net/problem/10828

import sys

count = int(sys.stdin.readline())
st = []
print_list = []

for i in range(count):
    command = str(sys.stdin.readline().rstrip())

    if command[-1].isdecimal():
        st.append(command.split()[1])
        
    if command == "pop":
        if len(st) > 0 :
            print_list.append(st[len(st) - 1])
            st.pop()
        else:
            print_list.append("-1")

    if command == "size":
        print_list.append(len(st))

    if command == "empty":
        if len(st) > 0 :
            print_list.append("0")
        else:
            print_list.append("1")

    if command == "top":
        if len(st) > 0 :
            print_list.append(st[len(st) - 1])
        else:
            print_list.append("-1")

for j in print_list:
    print(j)