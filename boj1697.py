import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())
visited = [False] * (100001)
# print(visited)
'''
q = deque()
q.append((n,0))
num = []
for i in range(k+1):
    num.append(i)
while q:
    a,b = q.popleft()
    if a == k:
        print(b)
        break
    a1 = a + 1
    a2 = a - 1
    a3 = a * 2
    if a1 in num:
        q.append((a1,b+1))
        num.remove(a1)
    if a2 in num:
        q.append((a2,b+1))
        num.remove(a2)
    if a3 in num:
        q.append((a3,b+1))
        num.remove(a3)
    
    
    # 5 일때 -> 4 6 10
    # 4일때 -> 5 
'''
cnt = 0
def bfs(visited,x):
    visited[x] = True
    q = deque()
    q.append((x,0))
    while q:
        num,cnt = q.popleft()
        if num == k:
            print(cnt)
            break
        if num > 100001:
            continue
        num1 = num - 1
        num2 = num + 1
        num3 = num * 2
        if visited[num1] == False:
            q.append((num1,cnt+1))
            visited[num1] = True
        if visited[num2] == False:
            q.append((num2,cnt+1))
            visited[num2] = True
        if visited[num3] == False:
            q.append((num3,cnt+1))
            visited[num3] = True

bfs(visited,n)
# print(visited)