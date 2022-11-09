N = int(input())
cur = 2

while True:
    if N == 1 or N == 2:
        print(N)
        break

    cur *= 2

    if cur >= N:
        print((N - (cur >> 1)) << 1)
        break
