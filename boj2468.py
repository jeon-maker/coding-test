# BFS로 해당 숫자 이하의 것들은 방문처리 후 덩어리 구하기. 
# 덩어리 구하는 것은 숫자인 것들에만 이동 가능하게끔. 
# BFS 함수 한번 덩어리 구하는 함수 한번만들고, for 문 돌려서 탐색
import sys
input = sys.stdin.readline
import copy
n = int(input())
graph = [list(input().split()) for _ in range(n)]
graph2 = copy.deepcopy(graph)
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(graph,x,y,num):
    if int(graph[x][y]) <=num:
        graph[x][y] = '999'
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()
        if int(graph[a][b]) <=num:
            graph[a][b] = '999'
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                q.append((nx,ny))

def find_area(graph,x,y):
    que = deque()
    que.append((x,y))
    while que:
        a,b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!= '999':
                graph[nx][ny] = '999'
                que.append((nx,ny))
ans = []
cnt = 0
# for i in range(1,101):
#     bfs(graph,0,0,i)
#     for j in range(n):
#         for k in range(n):
#             if graph[j][k] != '999':
#                 find_area(graph,j,k)
#                 cnt+=1
#     ans.append(cnt)
#     cnt = 0
#     graph = graph2
# print(max(ans))

for p in range(0,101):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if int(graph[i][j]) <= p:
                graph[i][j] = '999'
    for ii in range(n):
        for jj in range(n):
            if graph[ii][jj] != '999':
                find_area(graph,ii,jj)
                cnt+=1
    # print(graph)
    graph = copy.deepcopy(graph2)
    ans.append(cnt)
    # print(graph)
    
print(max(ans))