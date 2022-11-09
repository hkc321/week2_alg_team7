# https://www.acmicpc.net/problem/3190

# import sys

# head = [0,0] # 시작위치
# tail = [0,0]
# apple_loca = []
# turn_time = []
# time = 0
# mode = 3
# turn_idx = 0
# apple_idx = 0



# # 보드 크기
# size = int(sys.stdin.readline())

# # 사과 갯수
# apple_count = int(sys.stdin.readline())

# # 사과 위치
# for i in range(apple_count):
#     apple_loca.append(list(map(int,sys.stdin.readline().split())))

# # 방향전환 횟수
# turn = int(sys.stdin.readline())

# # 전환시점
# for i in range(turn):
#     turn_time.append(list(map(str,sys.stdin.readline().split())))

# print(turn_time)

# while True:
#     time += 1
    
#     ### 방향전환 체크##
#     if time == int(turn_time[turn_idx][0]):
#         if turn_time[turn_idx][1] == "D":
#             mode += 3
#             if mode > 9:
#                 mode = 0
#         if turn_time[turn_idx][1] == "L":
#             mode -= 3
#             if mode < 0:
#                 mode = 9
#         if turn_idx < turn -1:
#             turn_idx += 1
    
#     if mode == 3:
#         head[0] += 1
#     if mode == 6:
#         head[1] += 1
#     if mode == 9:
#         head[0] -= 1
#     if mode == 0:
#         head[1] -= 1
    
#     if head == apple_loca[apple_idx]:


#     if (head[0] == 0 or head[0] == size - 1 or head[0] == tail[0]) or (head[1] == 0 or head[1] == size - 1 or head[1] == tail[1]):
#         print(time)
#         break
#     ### 사과 유무 체크###
#     ### 끝###
#     ### 벽에 부딪힘 체크##
#     ### 끝###
#     ### 끝####



import sys

head = 1 # 시작위치
tail = 1
apple_loca = []
turn_time = []
time = 0
mode = 3
turn_idx = 0
apple_idx = 0

q = []
front = 0
rear = 0



# 보드 크기
size = int(sys.stdin.readline())
board = [None] * (size * size)

# 사과 갯수
apple_count = int(sys.stdin.readline())

# 사과 위치
for i in range(apple_count):
    apple_loca.append(list(map(int,sys.stdin.readline().split())))

# 방향전환 횟수
turn = int(sys.stdin.readline())

# 전환시점
for i in range(turn):
    turn_time.append(list(map(str,sys.stdin.readline().split())))

print(turn_time)

while True:
    time += 1
    
    ### 방향전환 체크##
    if time == int(turn_time[turn_idx][0]):
        if turn_time[turn_idx][1] == "D":
            mode += 3
            if mode > 9:
                mode = 0
        if turn_time[turn_idx][1] == "L":
            mode -= 3
            if mode < 0:
                mode = 9
        
        if turn_idx < turn -1:
            turn_idx += 1
    
    # head 움직임
    if mode == 3:
        head += 1
    if mode == 6:
        head += size
    if mode == 9:
        head -= 1
    if mode == 0:
        head -= size
    
    q[rear] = head
    rear += 1

    # 사과 체크
    if head == (size * apple_loca[apple_idx][0]) - (size - apple_loca[apple_idx][1]):



    if (head[0] == 0 or head[0] == size - 1 or head[0] == tail[0]) or (head[1] == 0 or head[1] == size - 1 or head[1] == tail[1]):
        print(time)
        break
