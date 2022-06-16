'''
입력조건
첫번째 줄에 얾음 트르이 세로 길이n과 가로 길이 m이 주어진다.
두번째 줄부터 n+1 번째 줄 까지 얼음 틀의 형태가 주어진다
이때 구멍이 뚫려있으면 0 막혀있으면 1이다.

출력조건
한 번에 만들 수 있는 아이스크림의 개수를 출력한다
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

#for 문 사용해서 모든 요소에 접근을 하고 사방이 0일 경우 아이스크림 1개
#모든 요소에 접근을 어떻게 할 것인가?
#한번 접근하면 0으로 바꾸기! 그리고 다른 좌표로 접근하기 (사방으로)

'''
n , m = map(int,input().split())
case = []
stack = []
icecream = 0 # 하나의 덩어리가 나올때 마다 +1 시키기
for i in range(n) :
    case.append(list(map(int,input())))  # 한줄을 입력받고 이것을 전체로 리스트를 만들어서 append 하면 됨!

def dfs(x,y):
    global icecream
    print(case)
    if(x>m | y>n | x<0 | y<0 ):
        return False
    elif(case[x][y]==0):
        case[x][y]=1
        if(case[x-1][y]==1 & case[x+1][y]==1 & case[x][y-1]==1 & case[x][y+1]==1): #사이에 있는 값들에게만 
            icecream += 1

    elif(case[x][y]==1):
        return False

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)    
    return True

dfs(0,0)
print(icecream)
'''
i = 0
def reculsive(i):
    if(i==5):
        return False
    i += 1
    reculsive(i)
    print("now the i is : %d"%(i))


graph = [0,0,1]
def dfs(x):

    if(x>4):
        return False
    if(graph[x]==0):
        graph[x]=1

        dfs(x+1)
        print(x," try")

        print(graph)
        print(graph[x])
        return True
    return False


print(dfs(i))