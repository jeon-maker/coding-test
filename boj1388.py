import sys
input = sys.stdin.readline
n,m = map(int,input().split())
floor = [list(input().strip()) for _ in range(n)]
#floor 완성
# 
# " - " 탐색하는것 만들기
garo = 0
sero = 0
garo_count = []
for i in range(n):    
    for j in range(m):
        garo += 1
        if floor[i][j] =='-':
            garo_count.append(garo) #연속된 수면 하나로 판단하기. 수가 끊길때마다 가로 합 판단하기
    garo += 100
# print(garo_count)
#---###---  -> 123 789 성공

sero_count = []
for j in range(m):
    for i in range(n):
        sero+= 1
        if floor[i][j] =='|':
            sero_count.append(sero) #연속된 수면 하나로 판단하기. 수가 끊길때마다 가로 합 판단하기
    sero += 100        

hap = 0
def count(arr):
    if not arr:
        return False
    global hap
    hap+=1
    start = 0
    for k in range(len(arr)-1):
        cnt = arr[k]
        cnt_2 =arr[k+1]
        if cnt_2 - cnt != 1 :
            hap += 1
    return hap
count(garo_count)
count(sero_count)
print(hap)