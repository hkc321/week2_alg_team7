from sys import stdin


N = int(stdin.readline())

stack = []
result = 1

for i in range(N):
    stack.append(int(stdin.readline()))

curMax = stack[N - 1]
for i in range(N - 1, -1, -1):
    if stack[i] > curMax:
        result += 1
        curMax = stack[i]

print(result)
