# n = int(input())
# graph = [[]]
# popular_list = [[]]

# visited = [False] * (n+1)
# for i in range(1,n+1):
#     graph.append([])
#     popular_list.append([])
# popular_list_copy = popular_list    
# for i in range(1,n+1):
#     relation = str(input())
#     for j in range(n):
#         if relation[j] == 'Y':           
#             graph[i].append(j+1)           
# print (graph)
# #bfs로 깊이 1 까지만 가기.
# k = 0
# def dfs(graph,visited,v,start):
#     global k 

#     if k ==3:
#         return False
#     popular_list[start].append(v)
#     print("v : " ,v)
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             k += 1            
#             dfs(graph,visited,i,start)
            


# from collections import deque
# def bfs(graph,visited,v,start):
#     global k
#     visited[v] = True
#     queue = deque([v])
#     while queue:
#         if k==3:
#             return False
#         v = queue.popleft()
#         k+= 1
#         if v != start:
#             popular_list[start].append(v)
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# for i in range(1,n+1):
#     visited = [False] * (n+1)
#     popular_list = popular_list_copy

#     dfs(graph,visited,i,i)
#     print(popular_list)
# s = []
# for i in range(3):
#     s.append(list(input().strip()))

import sys
input = sys.stdin.readline
n = int(input())
s = []
visit = [[0]*n for i in range(n)]

def floyd():
    for k in range(n): #거치는 점
        for i in range(n): #시작 점
            for j in range(n): #끝 점
                if i==j:
                    continue #시작점과 끝점이 같다면 넘어가기
                if s[i][j] =='Y' or( s[i][k]=='Y' and s[k][j]=='Y'):
                    visit[i][j]=1
for i in range(n):
    s.append(list(input().strip()))
floyd()
result = 0 
for i in range(n):
    cnt =0
    for j in range(n):
        if visit[i][j] == 1:
            cnt += 1
    result = max(result,cnt)
print(result)