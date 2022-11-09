from sys import stdin


T = int(input())

for i in range(T):
    stack = []
    parens = input()
    for paren in parens:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else: 
        if not stack: 
            print("YES")
        else: 
            print("NO")
            