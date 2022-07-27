import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[]]
visited = [False] * (n+1) 
for i in range(n):
    graph.append([])
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,n+1):
    graph[i].sort()
# print(graph)
def dfs(graph,visited,v):
    print(v,end=" ")
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)
dfs(graph,visited,v)
print("")
visited = [False] * (n+1)

from collections import deque

def bfs(graph,visited,start):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph,visited,v)