n , m = map(int,input().split())
MAP = []
for i in range(n):
    #MAP 에 그래프 정보 넣기
    MAP.append(list(map(int,input().split())))
MAP_copy = MAP
# bfs 로 사방에 1이 한개 이상 또는 경계에 놓인 것들
# 의 좌표 후보들을 찾기
import graphlib
from itertools import permutations
import sys
sys.setrecursionlimit(10**5)

#방문 좌표 처리 위한 visited 배열
visited = []
for i in range(n):
    visited.append([])
    for j in range(m):
        visited[i].append([False])
val = []


# print (MAP)
# print (visited)

#후보군 뽑기 성공
def make_wall(x,y): #x에 n (세로) //  y에 m(가로)
    global MAP
    #후보군 넣을 배열
    option = []
    virus = []
    for i in range(y): #가로길이만큼 반복
        if (MAP[0][i]==0):
            option.append((0,i))
        if (MAP[x-1][i]==0):
            option.append((x-1,i))
    for i in range(x): #세로길이만큼 반복
        if(MAP[i][0]==0):
            option.append((i,0))
        if(MAP[i][y-1]==0):
            option.append((i,y-1))

    for i in range(1,x-1): #외곽을 제외한 세로 길이
        for j in range(1,y-1): #외곽을 제외한 가로 길이
            print(i,j)
            if(MAP[i][j]==0):
                # 8각에 1이 있으면 후보가 됨
                if (
                    MAP[i-1][j]==1 or 
                    MAP[i+1][j]==1 or 
                    MAP[i][j-1]==1 or 
                    MAP[i][j+1]==1 or
                    MAP[i+1][j+1]==1 or
                    MAP[i+1][j-1]==1 or
                    MAP[i-1][j-1]==1 or
                    MAP[i-1][j+1]==1 ):
                    option.append((i,j))
    option = set(option)                
    print(len(option))
    choice = list(permutations(option,3))
    choice.sort()
    print("choice: ")
    # 세균 위치 구하기 
    for i in range(x):
        for j in range(y):
            if(MAP[i][j]==2):
                virus.append((i,j))
    print(virus)
    
    for i in range(len(choice)):
        for j in range(3):
            q = choice[i][j][0]
            p = choice[i][j][1]
            MAP[q][p] = 1 # 벽 3개 세우기 까지 성공.
        for k in range(len(virus)):
            xx = virus[k][0]
            yy = virus[k][1]  
            find_0(bfs(xx,yy),x,y)
            MAP = MAP_copy
    print(min(val))           

    #         for k in range(len(virus)):
    #              xx = virus[k][0]
    #              yy = virus[k][1]
    #              print(find_0(bfs(xx,yy),x,y))
        #세균 위치 구한것으로 bfs 실행하고 0의 갯수 리스트에 넣기


# 세균이 퍼져나가는 것 구현하기
def bfs(x,y): # x : 세로길이 n ,, y: 가로길이 m
    if(x <= -1 or n <= x or y <= -1 or m <= y ):
        return False
    if( MAP[x][y]==0 ):
        MAP[x][y] = 2
        bfs(x-1,y)
        bfs(x+1,y)
        bfs(x,y-1)
        bfs(x,y+1)
        return True
    elif(MAP[x][y]==1):
        return False
    return MAP
# 0의 갯수 구하는 함수
def find_0(graph,n,m):
    howmany0 = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j]==0):
                howmany0 += 1
    val.append(howmany0)

make_wall(n,m)
