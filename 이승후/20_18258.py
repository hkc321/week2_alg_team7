from sys import stdin
from collections import deque


N = int(input())
queue = deque([])

for i in range(N):
    command = stdin.readline().split()
    length = len(queue)

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if length == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(length)
    elif command[0] == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if length == 0:
            print(-1)
        else:
            print(queue[length - 1])
