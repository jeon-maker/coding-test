import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(input().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 1

def dfs(graph,x,y):
    global cnt
    graph[x][y] = cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] =='1':
            dfs(graph,nx,ny)

from collections import deque

# bfs 의 cnt로 가야한다..
def bfs(graph,x,y):
    global cnt
    graph[x][y] = '1'
    q = deque()
    q.append((x,y,1))
    while q:
        a,b,c = q.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] =='1':
                cnt = c + 1
                q.append((nx,ny,cnt))
                graph[nx][ny] = cnt
                
bfs(graph,0,0)
print(graph[n-1][m-1])