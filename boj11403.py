'''
방향성이 존재하는 인접행렬
그래프를 만들어놓고, 인접한 곳에서
BFS로 탐색하자. 가능한 모든 곳에
방향성이 있으니까
'''
import sys 
input = sys.stdin.readline
n = int(input())
graph = [list(input().split()) for _ in range(n)]

ans = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
# print("graph : ")
# print(graph)
# print("ans")
# print(ans)

from collections import deque

def bfs(graph,x,c):
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        for i in range(n):
            if graph[a][i] == '1':
                if visited[c][i] == 0:
                    
                    ans[c][i] = 1 # 0,1 / 
                    visited[c][i] = 1 # 0,1 / 

                    q.append((i))   # 1,4 -> 4,5 / 4,6 -> 5,1 / 6,7 -> 1,4 / 7,3 -> 

for i in range(n):
    bfs(graph,i,i)
    visited = [[0] * n for _ in range(n)]
for i in range(n):
    print(*ans[i])