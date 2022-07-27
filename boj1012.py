import sys
input = sys.stdin.readline
T = int(input())
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(graph,a,b):
    # visited[a][b] = True
    graph[b][a] = 0
    que = deque()
    que.append((a,b))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < M and 0<=ny < N :
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    que.append((nx,ny))                   
for i in range(T):
    cnt = 0
    M,N,K =map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    # visited = [[False] *M for _ in range(N)] 
    for j in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1
    for i2 in range(M):
        for j2 in range(N):
            if graph[j2][i2] == 1:
                bfs(graph,i2,j2)
                cnt+= 1
    print(cnt)


    