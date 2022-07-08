from collections import deque
import sys
n,m,k,x = map(int,sys.stdin.readline().split())

visited = [False] * (n+1)

graph = [[]]
minimum_cost= [[]]

for i in range(n+1):
    graph.append([])
    minimum_cost.append([])
for i in range(m):
    s,t = map(int,sys.stdin.readline().split())
    graph[s].append(t)

# print(graph)
#
def bfs(graph,start,visited,minimum_cost,val):
    cnt = 0
    visited[start]=True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        cnt +=1 #cnt를 언제 증가시키느냐가 문제이다.
        # print(v,end=" ")
        for i in graph[v]:
            # print(v, " all i is ",i)
            if not visited[i]:
                print( "now v : ",v," now i : ",i , " now cnt : ",cnt)
                queue.append(i)
                minimum_cost[cnt].append(i)
                visited[i]=True
    arr_ = []
            
    if minimum_cost[val] ==[]:
        print(-1)
    else :
        for i in minimum_cost[val]:
            arr_.append(i)
        arr_.sort()
        for j in range(len(arr_)):
            print(arr_[j])

    
#cnt가 최단거리로 파악가능함.

bfs(graph,x,visited,minimum_cost,k)