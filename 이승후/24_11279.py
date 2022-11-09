from sys import stdin
import heapq


N = int(stdin.readline())
maxHeap = []

for i in range(N):
    userInput = int(stdin.readline())
    length = len(maxHeap)
    if userInput > 0:
        heapq.heappush(maxHeap, -userInput)
    else:
        if length > 0:
            print(-heapq.heappop(maxHeap))
        else:
            print(0)
