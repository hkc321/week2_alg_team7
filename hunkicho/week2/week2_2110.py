# https://www.acmicpc.net/problem/2110

# import sys

# house, share = list(map(int, sys.stdin.readline().split()))
# house_point = [0] * house

# for i in range(house):
#     house_point[i] = int(sys.stdin.readline())

# house_point.sort()

# pl = 0
# pr = len(house_point) - 1
# pc = pr // 2
# distance = 0
# check = 0

# while check > 3:
#     a = house_point[pc] - house_point[pl]
#     b = house_point[pl] - house_point[pc]
#     c = a if a > b else b

#     if c > distance:
#         distance = c

#     if check == 1:
#         pc = (pr // 2) + 1
#         check += 1
#     else:
#         pc = (pr // 2) - 1
#         check += 1
# print(distance)

import sys

house, share = list(map(int, sys.stdin.readline().split()))
house_point = [0] * house

for i in range(house):
    house_point[i] = int(sys.stdin.readline())

house_point.sort()