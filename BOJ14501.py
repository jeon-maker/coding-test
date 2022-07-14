'''
그래프를 먼저 만들자. 연결된 노드들의 그래프를 만드는데,
이때 후반기에 날짜가 지나는 것들은 제외한다.

'''
n = int(input())
graph = [[]]
visited = [False] * (100)
for i in range(1,n+1):
    graph.append([])
    a,b = map(int,input().split())
    if (a+i) > (n+1):
        b = 0
    graph[i].append((a,b))
  


# for i in range(1,n+1):
#     finishday = i + graph[i][0][0]
#     if finishday > n:
#         graph[i][0][1] = 0
        
cost = 0
def dfs(graph,visited,v):
    if v>n :
        # print(" exceed n ")
        return False
    global cost
    visited[v]=True #방문처리
    i = (v + graph[v][0][0]) # i의 범위가 선택 가능해야함 꼭 지정된것은 아님. 리스트로 바꿔보자.
    # print(" v : ",v)
    cost += graph[v][0][1]
    # print(" cost : ",cost)
    if not visited[i]: #방문하지 않은 곳이라면
            # visited[i] = True #방문처리
            dfs(graph,visited,i) 
            #여기서 추가할 것은 연결된 노드를 찾는 기능, 
            # 간선의 cost를 구하는 기능, 
            # 후반기에 초과 근무 하는것을 제외하는 기능
    return cost    
cost_hap = []
for i in range(1,n+1):
   cost_hap.append(dfs(graph,visited,i))
   cost = 0 
print(max(cost_hap))