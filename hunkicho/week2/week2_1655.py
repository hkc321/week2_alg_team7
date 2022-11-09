# https://www.acmicpc.net/problem/1655

import sys

count = int(sys.stdin.readline())
q = []
print_list = []

def enqueue(n):
    q.append(n)
    last_idx = len(q) - 1

    while last_idx >= 0:
        parent_idx = (last_idx - 1) // 2
        if parent_idx >= 0 and q[parent_idx] < q[last_idx]:
            q[last_idx], q[parent_idx] = q[parent_idx], q[last_idx]
            last_idx = parent_idx
        else:
            break
    print(q)
    if len(q) % 2 == 0:
        print_list.append(q[len(q) // 2 ])
    else:
        if len(q) == 1:
            print_list.append(q[0])
        else:
            print_list.append(q[(len(q) // 2) + 1 ])


for _ in range(count):
    enqueue(int(sys.stdin.readline()))

print("#######")
for i in print_list:
    print(i)
