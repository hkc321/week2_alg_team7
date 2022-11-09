from sys import stdin


N, C = map(int, stdin.readline().split())
H = sorted([int(input()) for i in range(N)])

lo = 0
hi = H[N - 1]

if C == 2:
    print(hi - H[0])
else:
    while lo <= hi:
        mid = (lo + hi) >> 1
        cur = H[0]
        count = 1

        for i in range(N):
            if H[i] - cur >= mid:
                cur = H[i]
                count += 1

        if count >= C:
            lo = mid + 1
        else:
            hi = mid - 1

    print(hi)
