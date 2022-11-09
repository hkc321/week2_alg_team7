from sys import stdin
import heapq

N = int(stdin.readline())
minHeap = []
maxHeap = []

for i in range(N):
    userInput = int(stdin.readline())
    if i == 0:
        heapq.heappush(minHeap, userInput)
        heapq.heappush(maxHeap, -userInput)
        print(-maxHeap[0])
        continue

    if i % 2 == 1:
        if minHeap[0] <= userInput:
            heapq.heappush(minHeap, userInput)
        else:
            heapq.heappush(maxHeap, -userInput)
            heapq.heappop(maxHeap)

            heapq.heappush(minHeap, -maxHeap[0])

    else:
        if minHeap[0] <= userInput:
            heapq.heappush(minHeap, userInput)
            heapq.heappop(minHeap)

            heapq.heappush(maxHeap, -minHeap[0])
        else:
            heapq.heappush(maxHeap, -userInput)

    print(-maxHeap[0])
