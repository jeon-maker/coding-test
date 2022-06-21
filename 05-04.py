'''
미로탈출 1인 곳으로만 이동 가능
입력예시
5 6
101010
111111
000001
111111
111111

출력예시
10
'''
#DFS 로 풀 수 있을듯.
#재귀함수 이용해보기

from ctypes import sizeof


n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input()))) #그래프 완성

#0,0 부터 n,m까지 1인 칸을 찾아 탐색해나가야 함. 
#
#이동할 때 마다 가까운 노드의 값을 +1 시키며 이동하면 목표 노드에 도달했을 때 노드의 값이 이동 횟수가 된다.
i = 0
def bfs(x,y,i):
    if (x<= -1 or y<= -1 or n <= x or m <= y): 
        return False
    if(graph[x][y]==1):
        i += 1
        graph[x][y]=i
        print(graph)
        bfs(x-1,y,i)
        bfs(x+1,y,i)
        bfs(x,y-1,i)
        bfs(x,y+1,i)
        
        return True
    return i
# for i in range(n):
#     for j in range(m):
#         bfs(i,j)
bfs(0,0,0)
print(graph[n-1][m-1])