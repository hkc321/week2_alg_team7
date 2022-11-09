# infix to postfix with stack
# https://www.youtube.com/watch?v=G9ujrSGEB4A

import sys

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

class ArrayStack:

    def __init__(self):           # 객체 생성 시 리스트 초기화
        self.data = []

    def size(self):       
        return len(self.data)     # 스택 길이 반환

    def isEmpty(self):            # 스택 비어있는지 여부 반환
        return self.size() == 0

    def push(self, item):         # 스택에 값 추가
        self.data.append(item)

    def pop(self):                # 맨 나중에 들어온 값 제거
        return self.data.pop()

    def peek(self):               # 맨 나중에 들어온 값 반환
        return self.data[-1]

def convert_to_postfix(S):        # infix to postfix
    opStack = ArrayStack()
    answer = ''
    
    for w in S :
        if w in prec :             # 문자가 *, /, +, -, ( 중 하나이면
            if opStack.isEmpty() : # 스택이 비어있으면 push
                opStack.push(w)    
            else :
                if w == '(' :          # 스택에 값 있을때는 (만 바로 push
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) :   # 현재 문자의 우선순위가 스택 맨 위의 우선순위 보다 클 때 까지 반복
                        answer += opStack.pop()                       # 스택에서 pop한 값을 리턴 문자열에 저장
                        if opStack.isEmpty() : break                  # 스택이 비어 있으면 반복문 종료
                    opStack.push(w)                                   # 반복문 종료 후 스택에 현재 문자 push
        elif w == ')' :            # 문자가 ) 일 경우
            while opStack.peek() != '(' :      # (가 나올 때 까지
                answer += opStack.pop()        # 스택에서 pop한 값을 리턴 문자열에 저장
            opStack.pop()                      # 이후 ( pop
        else :                     # 나머지 문자들은 그냥 리턴문자열에 저장
            answer += w
    
    while not opStack.isEmpty() :  # 스택에 남은 문자열이 있다면
        answer += opStack.pop()    # 리턴문자열에 차례대로 저장
    
    return answer

def calculate(tokens):
    stack = ArrayStack()
    for token in tokens:
        if token == '+':                              # +는 맨 위 2개의 값을 pop하여 + 후 다시 push
            stack.push(stack.pop()+stack.pop())
        elif token == '-':                            # -는 맨 위 2개의 값을 pop하여 - 후 다시 push
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':                            # *는 맨 위 2개의 값을 pop하여 * 후 다시 push
            stack.push(stack.pop()*stack.pop())
        elif token == '/':                            # /는 제수가 맨 위에 있으므로 먼저 제수를 pop하여 저장해 놓고 그 다음 피제수를 pop하여 / 후 다시 push
            rv = stack.pop()
            stack.push(stack.pop()/rv)
        else:                                         # 숫자는 스택에 push
            stack.push(int(token))
    return stack.pop()

infix = sys.stdin.readline().replace("\n", "").replace(" ","")

postfix = convert_to_postfix(infix)

print(f"postfix : {postfix}")

result = calculate(postfix)

print(f"result : {result}")