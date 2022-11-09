# https://www.acmicpc.net/problem/9012

import sys

st = []
open = []
close = []
number = int(sys.stdin.readline())

for i in range(number):
    check = list(sys.stdin.readline().rstrip())

    

    if check.count('(') == check.count(')'):
        st.append("YES")
    else:
        st.append("NO")

for j in st:
    print(j)