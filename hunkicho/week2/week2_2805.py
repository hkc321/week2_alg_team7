# https://www.acmicpc.net/problem/2805

# import sys
# count, length = list(map(int, sys.stdin.readline().split()))
# tree = list(map(int, sys.stdin.readline().split()))
# cut = 0

# tree.sort(reverse=True)

# for i in range(len(tree)):
#     cut += tree[i] - tree[i+1]
#     if cut >= length:
#         if cut == length:
#             print(tree[i+1])
#         else:
#             print(tree[i+1] + (cut - length))
#         break
    

import sys

def bin_search(arr, src):
    pl = 0
    pr = max(arr)
    

    while pl <= pr:
        pc = (pl + pr) // 2
        hap = 0


        for i in arr:
            if i > pc:
                hap += i - pc
        print("pl=",pl,"pr=",pr,"pc=",pc,"hap=",hap)

        if hap > src:
            pl += 1
        else:
            pr -= 1
    print(pr)

count, length = list(map(int, sys.stdin.readline().split()))
tree = list(map(int, sys.stdin.readline().split()))

cut = 0

tree.sort()
bin_search(tree,length)


# n,m =map(int,sys.stdin.readline().split())
# lis = list(map(int, sys.stdin.readline().split()))

# le=1
# ri=max(lis)

# while le<=ri:
#     mid = (le+ri)//2
#     total= [tree-mid if tree>mid else 0 for tree in lis]
#     # print(total)
#     total_val = sum(total)
#     # for tree in lis:
#     #     if tree>mid:
#     #         total+=(tree-mid)
#     if total_val>=m:
#         le=mid+1
#     else:
#         ri=mid-1

# print(ri)    