# https://www.acmicpc.net/problem/1715

import sys
q = []

def enqueue(n):
    q.append(n)
    last_idx = len(q) - 1

    while last_idx >= 0:
        parent_idx = (last_idx - 1) // 2
        if parent_idx >= 0 and q[parent_idx] > q[last_idx]:
            q[last_idx], q[parent_idx] = q[parent_idx], q[last_idx]
            last_idx = parent_idx
        else:
            break

def dequeue():
    last_idx = len(q) - 1
    if last_idx < 0:
        return 0
    q[0], q[last_idx] = q[last_idx],q[0]
    value = q.pop()
    maxheap_ify(q,0)

    return value

def maxheap_ify(q,idx):
        left = (idx * 2) + 1
        right = (idx * 2) + 2
        max_idx = idx

        if left <= len(q) - 1 and q[max_idx] > q[left]:
            max_idx = left
        
        if right < len(q) - 1 and q[max_idx] > q[right]:
            max_idx = right

        if max_idx != idx:
            q[idx], q[max_idx] = q[max_idx],q[idx]
            maxheap_ify(q,max_idx)
    


count = int(sys.stdin.readline())
check = 0
hap = 0 
asd = []

for _ in range(count):
    enqueue(int(sys.stdin.readline()))

if len(q) == 0:
    print(0)
else:
    while len(q) > 1:
        t1 = dequeue()
        t2 = dequeue()
        hap += t1 + t2
        enqueue(t1 + t2)
    # for i in range(len(q) - 1):
    #     if i != 0:
    #         hap += hap + dequeue()
    #     else:
    #         hap = dequeue() + dequeue()

    print(hap)