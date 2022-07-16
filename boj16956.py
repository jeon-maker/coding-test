# import sys
# input = sys.stdin.readline
# R,C = map(int,input().split())
# visit = [[0] * C for _ in range(R)]
# MAP = [list(input().strip()) for _ in range(R)]
# print(MAP[0][0])

# def make_wall(MAP,i,j):
#     if (i>=R or i<= -1 or j >= C or j <= -1):
#         return False
#     if MAP[i][j] =='S':
#         return False
#     elif MAP[i][j] == '.':
#         MAP[i][j] = 'D'

# for i in range(R):
#     for j in range(C):
#         if MAP[i][j] =='S':
#             print("s point : ",i,j)
#             make_wall(MAP,i+1,j)
#             make_wall(MAP,i-1,j)
#             make_wall(MAP,i,j+1)
#             make_wall(MAP,i,j-1)

# print("make wall graph : ")
# print(MAP)

# def wolf_moving(MAP,i,j):
#     if (i>=R or i<= -1 or j >= C or j <= -1):
#         return False
#     if MAP[i][j]=='W':
#         return False
#     elif MAP[i][j] =='S':
#         print("wolf eat sheep")
#     elif MAP[i][j] == 'D':
#         MAP[i][j] =='@'
#     elif MAP[i][j] =='.':
#         MAP[i][j] = 'W'
#     elif MAP[i][j] == '@':
#         return False

# for i in range(R):
#     for j in range(C):
#         if MAP[i][j]=='W':
#             wolf_moving(MAP,i-1,j)
#             wolf_moving(MAP,i+1,j)
#             wolf_moving(MAP,i,j+1)
#             wolf_moving(MAP,i,j-1)
# print("after wolf moving : ")
# print(MAP)
import sys
input = sys.stdin.readline
R, C =map(int,input().split())
MAP = [list(input().strip()) for _ in range(R)]
sign = False #TRUE 면 늑대가 양한테 갈 수 있음

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'W': #늑대일 경우
            dx = [-1,1,0,0] #상하
            dy = [0,0,-1,1] #좌우

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<R and 0<=ny<C and MAP[nx][ny]=='S':
                    sign = True
                    break
        elif MAP[i][j] == 'S':
            pass
        elif MAP[i][j] == '.':
            MAP[i][j] = 'D'
if sign==True:
    print(0)
else:
    print(1)
    for i in MAP:
        print("".join(i))