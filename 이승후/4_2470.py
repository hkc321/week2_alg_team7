from sys import stdin


N = int(input())
H = [list(map(int, stdin.readline().split())) for i in range(N)]

lo = 0
hi = N - 1
threshold = 2147483647
result = []

while lo < hi:
    cur = H[lo] + H[hi]

    if abs(cur) < threshold:
        threshold = abs(cur)
        result = [H[lo], H[hi]]

    if cur < 0:
        lo += 1
    else:
        hi -= 1

print(result[0], result[1])
