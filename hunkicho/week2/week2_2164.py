# https://www.acmicpc.net/problem/2164

# import sys

# count = int(sys.stdin.readline())
# no = count
# q = [None] * 5000001
# front = 0
# back = count


# for i in range(count):
#     q[i] = i + 1


# while True:
#     print("버리는 거",q[front])
#     front += 2
#     if front == count - 1:
#         front = 0
#     no -= 1
#     if no == 1:
#         print(q[front])
#         break
#     q[back] = q[front]
#     print("버리고 난 후",q[front])
#     back += 1
#     if back == count - 1:
#         back = 0


# import sys

# count = int(sys.stdin.readline())
# no = count
# q = [None] * 5000001
# front = 0
# back = count


# for i in range(count):
#     q[i] = i + 1

# 4
# while True:
#     print("front=",q[front:back])
#     # 한장 버리고 front 다음 인덱스로
#     front += 1
#     if front == count - 1:
#         front = 0
#     no -= 1
#     print("no=",no)
#     if no == 1:
#         print(q[front])
#         break
#     # q[front]를 맨 뒤로
#     q[back] = q[front]
#     front += 1
#     back += 1
#     if back == count - 1:
#         back = 0



# import sys

# count = int(sys.stdin.readline())
# no = count
# q = [None] * 5000001
# front = 0
# back = count

# for i in range(count):
#     q[i] = i + 1

# while True:
#     # 한장 버리고 front 다음 인덱스로
#     front += 1
#     if front == count:
#         front = 0
#     no -= 1
#     if no == 1:
#         print(q[front])
#         break
#     # q[front]를 맨 뒤로
#     q[back] = q[front]
#     front += 1
#     back += 1
#     if back == count:
#         back = 0


import sys

count = int(sys.stdin.readline())
if count == 1:
    print(1)
    exit()
no = count
q = [None] * 5000000
front = 0
back = count

for i in range(count):
    q[i] = i + 1

while True:
    # 한장 버리고 front 다음 인덱스로
    front += 1
    # if front == count:
    #     front = 0
    no -= 1
    if no == 1:
        print(q[front])
        break
    # q[front]를 맨 뒤로
    q[back] = q[front]
    front += 1
    back += 1
    # if back == count:
    #     back = 0