'''
N * M 크기의 얼음 틀
구멍이 뚫려 있는 부분은 0 칸막이가 존재하면 1
상하좌우 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
얼음틀의 모양이 주어졌을 때, 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성.

입력조건
첫 번째 줄에 얼음 틀의 세로길이 n 과 가로 길이 M이 주어진다.
두 번때 줄부터 N+1번째 줄까지 얼음틀의 형태가 주어진다.
이때 구멍이 뚫려있으면 0 그렇지 않으면 1이다.

출력조건
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

입력 예시
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

출력예시
8
'''

# 문제 해설 
#얼음을 얼릴 수 있는 공간이 상 하 좌 우로 연결되어 있다고 표현가능이기 때문에
#그래프 형태로 모델링 할 수 있다.
#1. 특정한 지점의 주변 상 하 좌 우를 살펴본 뒤에 주변 지점 중에서 
# 값이 0 이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다
#2.방문한 지점에서 다시 상 하 좌 우를 살펴보면서 방문을 다시 진행하면 연결된 모든 
#지점을 방문할 수 있다.
#3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다


# N, M을 공백으로 구분하여 입력받기
n,m = map(int,input().split())

#2차원 리스트의 맵 정보 입력받기
# 이 부분을 기억할 것, 2차원 배열로 입력받는 형식으로, DFS에 쓸 수 있다는 것을 기억하자.
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #범위에 알맞는 설정 해주가
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #방문 처리
        graph[x][y] = 1
        #상 하 좌 우 위치 모두 재귀 호출 즉, 주변에 연결되어 있는 0을 다 1로 바꿔주며 True 값을 반환함.
        #아이스크림 하나 전부를 탐색할 때 이미 True값이 되는 것임.
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1) #주변을 다 1로 바꾸고 나서 
        return True #true값을 반환 한번 함.
    return False

#모든 위치에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        print(i,j,dfs(i,j))
        if dfs(i,j) == True: # 아이스크림 하나 전부를 탐색할 때 이미  True값!
            result += 1

print(result)

