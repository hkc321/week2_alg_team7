from sys import stdin


A, B, C = map(int, stdin.readline().split())


def multiply(a: int, b: int) -> int:
    if b == 1:
        return a % C
    else:
        mul = multiply(a, b >> 1)
        if b % 2 == 0:
            return (mul * mul) % C
        else:
            return (mul * mul * a) % C


print(multiply(A, B))
