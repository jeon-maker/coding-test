import sys
from turtle import right
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    x,y = map(int,input().split())
    graph.append((x,y))
graph.sort()
point = []
most_h = 0
# print(graph)
for i in range(n):
    most_h = max(most_h,graph[i][1])
    if most_h == graph[i][1]:
            point.append(i) #맨 마지막에 들어간 j는 가장 높은 높이임 . point에는 x값들이 들어가 있음. 그래프의 인덱스를 넣어야함.
            # print(graph[i][0],graph[i][1])
most_h_idx = point[-1] #번호. 그래프의 인덱스가 들어가있음.
# print(most_h_idx)
second_h = 0
second = False



for i in range(most_h_idx+1,n):
    second_h = max(second_h,graph[i][1])
    if second_h == graph[i][1]:
        second_idx = i
        second = True
#point에는 idx가 순서대로 다 들어가 있음. 이제 idx를 통해 넓이를 구하는 것만 완성하면 됨.
# print(point)
s = 0
for i in range(len(point)-1):
    s += graph[point[i]][1] * (graph[point[i+1]][0]-graph[point[i]][0])
         # print(graph[point[i]][1]," * ",graph[point[i+1]][0]," -" ,graph[point[i]][0])
    s += graph[most_h_idx][1]
if second:
    s += (graph[second_idx][0] - graph[most_h_idx][0]) * graph[second_idx][1]
print(s)

#최고점을 기준으로 오른쪽 내림차순인 경우에만 s 구하고, 그렇지 않은 경우 second_h 구하기
right_sect = []
for i in range(most_h_idx+1,n):
    right_sect.append((graph[i]))
right_point = []
right_sect.sort(key = lambda x:-x[1])
for i in range(len(right_sect)):
    right_point.append(right_sect[i][0]) # 높이 순서로 인덱스가 들어가있음
arr = []
for i in range(len(right_point)-1):
    # 지금 right point에는 내림차순 높이 순서로 인덱스가 들어가 있음. 인덱스가 더 오른쪽에 있을 경우 ( 더 크면 ) 만 살아남음. 예를들어 8 10 9 11 면 8 10 만 살아남을 수 있음.
    if right_point[i] < right_point[i+1]:
        arr.append[i]
    

'''
인덱스가 증가하면서 높이가 커질경우 순조롭게 높이를 구할 수 있다.
일단 가장 큰 인덱스까지 증가하는 높이를 구한다.
그 다음 남은 오른쪽 인덱스가 오름차순일 경우 가장 큰 거 구해야하고, 내림차순일 경우 순조롭게 구할 수 있고..
남은 오른쪽 인덱스에 대해서 내림차순이 될 때만 순조롭게 구할 수 있다.
'''

