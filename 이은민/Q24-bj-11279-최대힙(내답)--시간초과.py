# https://www.acmicpc.net/problem/11279

import sys

def left(i: int):
    return 2 * i + 1

def right(i: int):
    return 2 * i + 2

def max_heapify(A: list, i: int):   
    l = left(i)          
    r = right(i)        
    heap_size = len(A)  
    largest = i
    if (l > heap_size-1):
        return A
    if (l == heap_size-1) and (A[l] > A[i]):
        largest = l
    if (l < heap_size-1):
        if (l <= heap_size) and (A[l] > A[i]):
            largest = l
        else:
            largest = i
        if (r <= heap_size) and (A[r] > A[largest]):
            largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        return max_heapify(A, largest)
    else:
        return A

def build_max_heap(A: list):    #[3,1,2,4]
    heap_size = len(A)          # 4
    if heap_size == 2:
        if A[0] < A[1]:
            A[0], A[1] = A[1], A[0]
        return A
    else:
        for i in range((heap_size//2)-1, -1, -1):  # 3인 경우, 0만 , 4->1,0
            max_heapify(A, i)

N = int(sys.stdin.readline())
A = []

for _ in range(N):
    input = int(sys.stdin.readline())
    heap_size = len(A)
    if input == 0:
        if heap_size == 0:
            print(0)
        elif heap_size < 3:
            print(A.pop(0))
        else:
            print(A.pop(0))
            build_max_heap(A)
    else:   # 정수를 삽입할 때 
        A.append(input)
        if heap_size >= 1:   # 노드가 0개만 존재 
            build_max_heap(A)  
