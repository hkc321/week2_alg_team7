from sys import stdin


K = int(input())

stack = []

for i in range(K):
    userInput = int(input())
    if userInput == 0:
        stack.pop()
    else:
        stack.append(userInput)
print(sum(stack))