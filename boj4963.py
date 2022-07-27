import sys
input = sys.stdin.readline
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(graph,x,y):
    graph[x][y] = '0'
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <h and 0<=ny<w:
            if graph[nx][ny]=='1':
                dfs(graph,nx,ny)

from collections import deque
def bfs(graph,a,b):
    graph[a][b] = '0'
    que = deque()
    que.append((a,b))
    while que:
        x,y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <h and 0<=ny<w:
                if graph[nx][ny]=='1':
                    que.append((nx,ny))
                    graph[nx][ny] = '0'
                    
    
cnts = []
while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    cnt = 0
    graph = []
    for i in range(h):
        graph.append(list(input().split()))
    # print(graph)
    # print(graph[0][0])
    for i in range(w): #가로 길이 두번째꺼
        for j in range(h): # 세로 길이 처음꺼
            if graph[j][i] == '1':
                # print("find 1")
                bfs(graph,j,i)
                cnt += 1
    cnts.append(cnt)
for i in range(len(cnts)):
    print(cnts[i])