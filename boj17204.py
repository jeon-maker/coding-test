import sys
input = sys.stdin.readline
n,m= map(int,input().split())
member = [[]]
visited = [False]*(n)
for i in range(n):
    member.append([])
    k = int(input())
    member[i].append(k)
#dfs 풀기
count = 0
called = []
def dfs(graph,visited,v):
    global count
    visited[v] = True
    # print(" v : ", v)
    called.append(v)
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)

dfs(member,visited,0)
# print(called)
find = False
num = 0
for i in range(len(called)):
    if called[i] == m:
        find = True
        num = i
if find :
    print(num)
else:
    print(-1)
    