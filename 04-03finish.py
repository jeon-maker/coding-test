'''
A는 북쪽으로부터 떨어진 칸의 개수 , B는 서쪽으로부터 떨어진 칸의 개수  ->(A,B)
1.현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정한다
2.캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3.만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고
1단계로 돌아간다. 단, 이대 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
입력조건 : 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3<=N , M<=50)
           둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
           방향d의 값으로는 다음과 같이 4가지가 존재한다
           0 북쪽 , 1 동쪽, 2 남쪽, 3 서쪽
           셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로
           각 줄의 데이터는 서쪽부터 동쪽대로 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어있다.
           0 - 육지 , 1 - 바다
출력조건 : 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
입력예시
4 4
1 1 0 
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
출력예시
3
'''

#n 세로크기 m 가로크기
from itertools import count
from re import A
from xmlrpc.client import boolean

n,m = map(int,input().split())
y, x, direction = map(int,input().split())
array2 = []
array3 = [] #한번 거친 좌표 넣기.
array3.append((y,x))
#입력받은 크기의 2차원 배열 생성. 기억하자. 세로 - 가로.  
#col: 열 , row : 행 여기서는 n 이 행이 되어야 함.(n이 세로 길이임.)
#4행 2열을 만들려면 4 2 순서대로 치면 됨.
# array = [[0 for col in range(m)] for row in range(n)]  # 세로 길이 = 행의 갯수 , 가로 길이 = 열의 갯수
# # print(array)
for i in range(n):
    array2.append(list(map(int,input().split()))) # 맵 정보 입력받기.
# print(array2[2][1]) #앞에가 세로 맞음
# array2에는 현재 map의 정보가 들어가 있음.
#왼쪽으로 도는 함수 만들기
def turn_left(direction):
    if direction == 0:
        direction = 3
    elif direction == 1:
        direction = 0
    elif direction == 2:
        direction = 1
    elif direction == 3:
        direction = 2
    return (direction)
#갈 수 있을지 없을지 판단하고 갈 수 있으면 가는 함수 만들기
count_ = 1 #이동 횟수 (시작때 이미 한칸 방문)
turn_count = 0 # 회전 횟수
direct = 0
def where_to_go( y, x , direction):
    global count_
    global turn_count
    global direct
    global a # y 넣기
    global b # x 넣기

    #현재 위치의 좌표를 뽑아내야 함.
    direct = turn_left(direction)
    north = 0
    south = 2
    east = 1
    west = 3
    turn_count +=1
    if direct == north:
        if boolean(array2[y-1][x] == 0) & boolean((y-1,x) not in array3): #육지이고 안가본 곳이라면
            y = y-1
            x = x
            count_ +=1
            array3.append((y,x))
            turn_count = 0
        elif array2[y-1][x] == 1 :
            pass
    if direct == south:
        if boolean(array2[y+1][x] == 0) & boolean((y+1,x) not in array3):
            y = y+1
            x = x
            count_ +=1
            array3.append((y,x))
            turn_count = 0
        elif array2[y+1][x] == 1:
            pass
    if direct == east:
        if boolean(array2[y][x+1] == 0) & boolean((y,x+1) not in array3):
            y = y
            x = (x+1)
            array3.append((y,x))
            count_ += 1
            turn_count = 0
        elif array2[y][x+1] == 1:
            pass
    if direct == west:
        if boolean(array2[y][x-1] == 0) & boolean((y,x-1) not in array3):
            y = y
            x = x-1
            count_ +=1
            array3.append((y,x))
            turn_count = 0
        elif array2[y][x-1] == 1:
            pass
    a = y
    b = x
    print("location :", a,b,"direct  : ",direct , "count_: ", count_ , "turn_count: ",turn_count, "visited: ",array3)
    return (count_ , a ,b , direct , turn_count) 
print("before y,x, direct : ",y,x,direction , "val : ",array2[y][x] )
where_to_go(y,x,direct)
while(True):
    where_to_go(a,b,direct)
    if(turn_count == 5):
        print(count_)
        break
print("after y,x, direct: ", a,b,direct, "val : ",array2[y][x] )



