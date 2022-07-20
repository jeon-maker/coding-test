import sys
input = sys.stdin.readline

n= int(input())
graph = [list(input().strip()) for _ in range(n)]
graph_copy = graph

# 한줄 빙고 찾는 함수 만들기
def bingo(graph):
    x_bingo = 1
    y_bingo = 1
    bingo = []
    for i in range(n):
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                y_bingo += 1
        bingo.append(y_bingo)    
        y_bingo = 1
    for i in range(n):
        for j in range(n-1):
            if graph[j][i] == graph[j+1][i]:
                x_bingo += 1
        bingo.append(x_bingo)
        x_bingo = 1
    return(max(bingo))
max_candy = []

for i in range(n):
    for j in range(n):
        dx = [ -1 , 1 , 0 , 0]
        dy = [ 0 , 0 , -1 , 1]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0<=nx<n and 0<=ny<n:                
                # print("x : ",i," nx : ",nx)
                # print("y : ",j," ny : ",ny)
                now = graph[i][j]
                next = graph[nx][ny] # 상 하 좌 우 다 들어감.
                graph[i][j] = next
                graph[nx][ny] = now
                # print("###graph###")
                # print(graph)
                val = bingo(graph)
                # print(val)
                graph[i][j] = now
                graph[nx][ny] = next
                max_candy.append(val)
                # graph = graph_copy

print(max(max_candy))