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


def bfs(x,y,i):
    if(x<=-1 | x>=m | y<=-1 | y>=n ):
        return False
    if(graph[x][y]==1):
        i += 1
        graph[x][y] = i #방문 처리 후
        # bfs(x,y-1) 
        # bfs(x,y+1) #아래
        # bfs(x-1,y)
        # bfs(x+1,y) #오른쪽
        bfs(x,y+1,i)
        bfs(x+1,y,i)
        bfs(x,y-1,i)
        bfs(x-1,y,i)
        #인접 노드의 값들을 이동 할 때 마다 1 씩 증가시킴
        return True

    if(x==n & y==m):
        print("끝!")
    return False

bfs(0,0,0)
