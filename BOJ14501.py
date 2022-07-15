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
print('graph')
print(graph)

# for i in range(1,n+1):
#     finishday = i + graph[i][0][0]
#     if finishday > n:
#         graph[i][0][1] = 0
cost = 0
def dfs(graph,visited,v):
    if v>n :
        # print(" exceed n ")
        return False
    visited[v]=True #방문처리
    i = (v + graph[v][0][0]) # i의 범위가 선택 가능해야함 꼭 지정된것은 아님. 리스트로 바꿔보자.
    #현재 i는 출발점을 의미함. 가능한 출발점부터 끝 지점까지 선택 가능하게 만들기.
    #그리고 개별 cost를 갖고 재귀함수가 되어야함.
    finish_point = n
    start_list = []
    for j in range(i,n+1):
        start_list.append(j)
    print(" v : ",v)
    global cost
    cost += graph[v][0][1]

    for i in start_list:
        # print( " i list : ", i )
        if not visited[i]: #방문하지 않은 곳이라면
            # visited[i] = True #방문처리
            print("next i : ",i)
            print(" cost : ",cost)

            dfs(graph,visited,i) 
            #여기서 추가할 것은 연결된 노드를 찾는 기능, 
            # 간선의 cost를 구하는 기능, 
            # 후반기에 초과 근무 하는것을 제외하는 기능
    
    return cost
ways = [ ]
def dfs2(graph,visited,v):
    # 가능한 루트를 기억해서 나중에 각각의 cost를 더하는 함수
    if v>n :
        return False
    visited[v]=True 
    i = (v + graph[v][0][0]) 
    start_list = []
    for j in range(i,n+1):
        start_list.append(j)
    print(" v : ",v)

    for i in start_list:
        # print( " i list : ", i )
        
        print("next i : ",i)
        print(" cost : ",cost)

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