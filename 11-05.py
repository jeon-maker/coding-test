'''볼링공 고르기
입력 예시
5 3
1 3 2 3 2
출력예시 
8

입력예시
8 5
1 5 4 3 2 4 5 2
출력예시
25

'''
from collections import deque

n,m,k,x = map(int,input().split())

visited = [False] * (n+1)

graph = [[]]
minimum_cost= [[]]

for i in range(n):
    graph.append([])
    minimum_cost.append([])
for i in range(m):
    s,t = map(int,input().split())
    graph[s].append(t)

# print(graph)
#
cnt = 0
def bfs(graph,start,visited,minimum_cost,val):
    global cnt
    visited[start]=True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        cnt +=1
        # print(v,end=" ")
        for i in graph[v]:
            # print(v, " all i is ",i)
            if not visited[i]:
                # print( "now i : ",i , " now cnt : ",cnt)
                queue.append(i)
                minimum_cost[cnt].append(i)
                visited[i]=True
    if minimum_cost[val] ==[]:
        minimum_cost[val] = -1

    for i in minimum_cost[val]:
        print(i)               
#cnt가 최단거리로 파악가능함.

bfs(graph,1,visited,minimum_cost,k)