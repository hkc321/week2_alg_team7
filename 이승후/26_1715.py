from sys import stdin
import heapq


N = int(stdin.readline())
minHeap = []
result = 0

for i in range(N):
    heapq.heappush(minHeap, int(stdin.readline()))

while len(minHeap) > 1:
    total = heapq.heappop(minHeap) + heapq.heappop(minHeap)
    heapq.heappush(minHeap, total)
    result += total

print(result)
