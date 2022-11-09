# https://www.acmicpc.net/problem/11279

import sys


class MaxHeap():
    def __init__(self):
        self.q = [None]

    def enqueue(self, n):
        self.q.append(n)
        last_idx = len(self.q) - 1

        while last_idx > 0:
            parent_idx = self.get_parent_idx(last_idx)
            if parent_idx > 0 and self.q[parent_idx] < self.q[last_idx]:
                self.swap(last_idx, parent_idx)
                last_idx = parent_idx
            else:
                break

    def dequeue(self):
        last_idx = len(self.q) - 1
        if last_idx < 1:
            return 0
        self.swap(1,last_idx)
        last = self.q.pop()
        self.maxheap_ify(1)
        return last

    def maxheap_ify(self,idx):
        left = self.get_lchild_idx(idx)
        right = self.get_rchild_idx(idx)
        max_idx = idx

        if left <= len(self.q) - 1 and self.q[max_idx] < self.q[left]:
            max_idx = left
        
        if right < len(self.q) - 1 and self.q[max_idx] < self.q[right]:
            max_idx = right

        if max_idx != idx:
            self.swap(idx, max_idx)
            self.maxheap_ify(max_idx)

            
    def get_parent_idx(self, idx):
        return idx // 2

    def get_lchild_idx(self, idx):
        return idx * 2

    def get_rchild_idx(self, idx):
        return idx * 2 + 1
    
    def swap(self,i,j):
        self.q[i], self.q[j] = self.q[j], self.q[i]

count = int(sys.stdin.readline())
print_list = []
mh = MaxHeap() 

for i in range(count):
    num = int(sys.stdin.readline())
    if num == 0:
        print_list.append(mh.dequeue())
    else:
        mh.enqueue(num)

for j in print_list:
    print(j)


# 인터넷 검색결과 heapq모듈을 사용해야 하는 것 같다.
# heappop, heappush는  최소힙만 동작하기 때문에 최대힙을 구현하기 위해서는 변형이 필요
# 넣어주는 값에 -1을 곱하여 heap에 push를 하면 가장 큰 값이 음수가 되어 가장 작은 값이 되어 최대 힙 구현이 가능
# heap에서 pop을 해 줄 때만 -1을 다시 곱하면 원래 숫자 출력 가능

# import sys
# import heapq
# n = int(input())
# heap = []
# for i in range(n):
#     a = int(sys.stdin.readline())
#     if a == 0:
#         if heap:
#             print((-1)*heapq.heappop(heap))
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap,(-1)*a)