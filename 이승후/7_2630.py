from sys import stdin


N = int(input())
H = [list(map(int, stdin.readline().split())) for i in range(N)]

results = []


def paper(x: int, y: int, N: int) -> None:
    cur = H[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if cur != H[i][j]:
                paper(x, y, N // 2)
                paper(x, y + N // 2, N // 2)
                paper(x + N // 2, y, N // 2)
                paper(x + N // 2, y + N // 2, N // 2)
                return
    if cur == 0:
        results.append(0)
    else:
        results.append(1)


paper(0, 0, N)
print(results.count(0))
print(results.count(1))
