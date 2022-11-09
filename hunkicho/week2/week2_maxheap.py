# 리스트로 최대 힙 구현
# i번 째 노드의 왼쪽 자식 노드의 위치는 (2i + 1)
# i번 째 노드의 오른쪽 자식 노드의 위치는 (2i + 2)
# i번 째 노드의 부모 노드의 위치는 (i-1 / 2)

class MaxHeap(object):
    def __init__(self):
        self.queue = []

    def insert(self, n):
        # 맨 마지막에 삽입할 원소를 임시로 추가
        self.queue.append(n)
        last_index = len(self.queue) - 1
        # 부모를 타고 올라가면서 크기를 비교
        while 0 <= last_index:
            parent_index = self.parent(last_index)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index)
        maxv = self.queue.pop()
        self.maxHeapify(0)  # root에서부터 재정렬
        print(maxv)
        return maxv

    # 임시 root 값부터 자식들과 값을 비교해나가며 재정렬하는 함수(max heap특성이 유지되도록 바꾸는 작업)
    def maxHeapify(self,i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        max_index = i  

        # 더 큰 값의 index를 넣어준다
        if left_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
            #print("2.maxl=",max_index)
        if right_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index
            #print("2.maxr=",max_index)

        # 만약 자신이 가장 큰게 아니라면 heapify
        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def parent(self, index):
        return (index - 1) // 2

    def leftchild(self, index):
        return index * 2 + 1

    def rightchild(self, index):
        return index * 2 + 2

    def printHeap(self):
        print(self.queue)

if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(1)
    mh.insert(3)
    mh.insert(11)
    mh.insert(6)
    mh.insert(5)
    mh.insert(2)
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
