import sys
from collections import Counter


def binarysearch(m: int, A: Counter) -> int:
    result = 0
    lo = 1
    hi = max(A)

    while lo <= hi:
        mid = (lo + hi) >> 1
        total = sum((tree - mid) * i for tree, i in A.items() if tree > mid)

        if total >= m:
            result = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return result


N, M = map(int, sys.stdin.readline().split())
A = Counter(sorted([int(i) for i in sys.stdin.readline().split()]))

print(binarysearch(M, A))
