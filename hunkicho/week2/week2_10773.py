# https://www.acmicpc.net/problem/10773

import sys

number = int(sys.stdin.readline())
st = []

for i in range(number):
    check = int(sys.stdin.readline())

    if check == 0:
        st.pop()
    else:
        st.append(check)

print(sum(st))