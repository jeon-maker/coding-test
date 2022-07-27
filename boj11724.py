import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(graph,visited,v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)
cnt = 0
from collections import deque

def bfs(graph,visited,v):
    visited[v] = True
    que = deque()
    que.append(v)
    while que:
        p = que.popleft()
        for k in graph[p]:
            if not visited[k]:
                que.append(k)
                visited[k] = True

for v in range(1,n+1):
    if not visited[v]:
        # dfs(graph,visited,v)
        bfs(graph,visited,v)
        cnt += 1
print(cnt)