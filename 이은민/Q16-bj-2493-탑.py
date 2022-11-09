# https://www.acmicpc.net/problem/2493

# 문제
# 일직선 위에 N개의 높이가 서로 다른 탑을
# 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고,
# 각 탑의 꼭대기에 레이저 송신기를 설치
# 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
# 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능

# 예를 들어 높이가 6, 9, 5, 7, 4
# 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사
# 높이가 4인 다섯 번째 탑에서 발사한 레이저 신호는 높이가 7인 네 번째 탑이 수신을 하고,
# 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이,
# 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다.
# 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.
# 탑들의 개수 N, 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내라.

# 입력
# 첫째 줄에 탑의 수를 나타내는 정수 N
# N은 1 이상 500, 000 이하
# 둘째 줄에는 N개의 탑들의 높이
# 탑들의 높이는 1 이상 100, 000, 000 이하의 정수

# 출력
# 첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력
# 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.

import sys

stack = []
tower = []
std = -1

def stack_structure(idx: int, input: int):
    global std

    if (len(stack) == 0):           # 1번탑일때
        stack.append((input, idx+1))
        tower.append(0)
    elif (input > stack[-1][0]):    # 새로 세워진 탑이 왼쪽 탑보다 클때
        while stack[-1][0] < input: # 새로 세워진 탑보다 작은 탑을 제거함
            stack.pop()
            if len(stack) == 0:
                break
        if len(stack) != 0:         # 제거하고 남은 더 큰탑을 추가 
            tower.append(stack[-1][1])
        else:
            tower.append(0)         # 더 큰 탑이 없으면 0 추가
        stack.append((input, idx+1))
    else:                           # 새로 세워진 탑이 왼쪽 탑보다 작을 때
        tower.append(stack[-1][1])
        stack.append((input, idx+1))


# 입력받기
N = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))

for idx, v in enumerate(input):
    stack_structure(idx, v)

print(" ".join(map(str, tower)))
