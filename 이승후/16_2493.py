from sys import stdin


N = int(stdin.readline())
tower = list(map(int, stdin.readline().split()))
stack = []
results = []

for i in range(N):
    while stack:
        top = len(stack) - 1
        if stack[top][1] > tower[i]:
            results.append(stack[top][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        results.append(0)
    stack.append([i, tower[i]])

print(" ".join(map(str, results)))
