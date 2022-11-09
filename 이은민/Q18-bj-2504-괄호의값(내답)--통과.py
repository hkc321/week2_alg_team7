# https://www.acmicpc.net/problem/2504
# 문제
# 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
    # 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’
    # 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
    # X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
    # 예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열
    # ‘([)]’ 나 ‘(()()[]’ 은 올바른 괄호열이 아니다. 
# 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다. 
    # ‘()’ 인 괄호열의 값은 2
    # ‘[]’ 인 괄호열의 값은 3
    # ‘(X)’ 의 괄호값은 2×값(X)
    # ‘[X]’ 의 괄호값은 3×값(X)
    # 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y)
    # 예를 들어 ‘(()[[]])([])’
    # ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22
    # 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28

# 입력
# 첫째 줄에 괄호열을 나타내는 문자열(스트링). 길이는 1 이상, 30 이하

# 출력
# 첫째 줄에 그 괄호열의 값을 나타내는 정수. 만일 입력이 올바르지 못한 괄호열이면 반드시 0

import sys

def right_bracket(input: str):
    stack = []
    for i in input:
        if (i == "(") or (i == "["):
            stack.append(i)
        else:
            if len(stack) != 0:
                if (i == ")") and (stack[-1] == "("):
                    stack.pop()  
                elif (i == "]") and (stack[-1] == "["):
                    stack.pop()  
            else:
                return 0
    if len(stack) != 0:
        return 0

# input = sys.stdin.readline().strip()
# input = '(()[[]])([])'.strip()  # 출력; 28
input = '[][]((])'.strip()    # 출력; 0
TF = right_bracket(input)

if TF != 0:
    stack = []
    answer = 0 
    temp = 1
    for i in range(len(input)):
        if input[i] == "(":
            stack.append(input[i])
            temp *= 2
        elif input[i] == "[":
            stack.append(input[i])
            temp *= 3
        elif input[i] == ")":
            if input[i-1] == "(":
                answer += temp
            stack.pop()
            temp //= 2          
        else:   # i == "]"
            if input[i-1] == "[":
                answer += temp
            stack.pop()
            temp //= 3          
    print(answer)
else: 
    print(TF)

