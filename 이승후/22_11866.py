from sys import stdin
from collections import deque


N, K = map(int, stdin.readline().split())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)

print('<', end='')
while queue:
    for i in range(K - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')

    if queue:
        print(',', end='')

print('>')
