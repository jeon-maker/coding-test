n = int(input())
m = int(input())
graph =[[]]
visited = [False] * (n+1)
for i in range(n):
    graph.append([])
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x) #서로 다 연결되어 있도록!

from collections import deque

hap = 0
def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    global hap
    for i in visited:
        if i == True:
            hap+=1
    if hap>= 1:
        hap -= 1
    print(hap)
bfs(graph,visited,1)