import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    que = deque(list(map(int,input().split())))
    count = 0
    while que:
        best = max(que)
        front = que.popleft()
        m -= 1

        if best == front:
            count += 1
            if m < 0:
                print(count)
                break
        else :
            que.append(front)
            if m < 0:
                m = len(que)-1