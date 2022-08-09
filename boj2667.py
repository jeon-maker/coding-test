import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

house = []
cnt = 1 # 단지별 집의 수
val = 0 # 단지의 갯수

def bfs(graph,x,y):
    global cnt
    graph[x][y] = 'S'
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()      
        for _ in range(4):
            nx = a + dx[_]
            ny = b + dy[_]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]=='1':
                cnt += 1
                q.append((nx,ny))
                graph[nx][ny] = cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            bfs(graph,i,j)
            val += 1
            house.append(cnt)
            cnt = 1
print(val)
house.sort()
for i in range(len(house)):
    print(house[i])