'''
체스판 나이트 이동 가능 방향
2개후 1개 
상 하 2개 좌 우 1개
좌 우 2개 상 하 1개 
nx ny 를 지정해서 목표물 나오면 stop
'''

from collections import deque
import sys
input = sys.stdin.readline

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2] # 나이트 이동 경로 케이스
cnt = 0


def bfs(graph,x,y):
    global cnt
    graph[x][y] = cnt
    visited[x][y] = 1
    q = deque()
    q.append((x,y,cnt))
    while q:
        a,b,c = q.popleft() #c는 원래 cnt
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0 and visited[nx][ny]==0:
                cnt = c + 1
                graph[nx][ny] = cnt
                visited[nx][ny] = 1
                q.append((nx,ny,cnt))

case = int(input())
for _ in range(case):
    n = int(input()) # 체스판 사이즈
    a,b = map(int,input().split()) # 시작 위치
    c,d = map(int,input().split()) #목표 위치
    
    graph = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    # print("graph ")
    # print(graph)
    bfs(graph,a,b)
    # print(graph)
    print(graph[c][d])
    cnt = 0





            
    
