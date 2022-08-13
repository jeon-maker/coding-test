import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
def solution(a,b,c,d,r): #x는 시작 y는 끝
    for i in range(n):
        for j in range(m):
            for _ in range(r):
                if i == a and j != c:
                    graph[i][j-1] = graph[i][j]
                elif i ==a and j == c:
                    graph[i+1][j] = graph[i][j]              
                elif i == b and j != d:
                    graph[i+1][j] = graph[i][j]
                elif i == b and j == d:
                    graph[i][j-1] = graph[i][j]
                elif i != b and j == d:
                    graph[i-1][j] = graph[i][j]
                elif i != b and j == a:
                    graph[i+1][j] = graph[i][j]
# a b c d 로 인자를 4개 받아야 할 것 같다.
# a b는 첫째 인덱스의 시작과 끝 범위 c d 는 둘째 인덱스의 시작과 끝 범위
# a b 