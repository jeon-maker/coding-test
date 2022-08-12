# 배열에 담아두고
# 숫자 크기가 최대 하중 이하일 경우에만 이동 가능한데.
# 한 트럭이 이동을 시작하면 초 세기 시작.
# 7 4 5 6 ...다리길이 2 최대 하중 10
# 7 혼자 2초 차지. 2초
# 4 5 동시 가능 두개라면 2 + 1 3초
# 6 2초 2초 다 건너기 다 건넌 후에는 +1초
# 가능한 묶음의 수를 센다 - > 7 45 6 --> 2초 3초 2초 +1 
# 10 묶음이니까 100 + 9 + 1
# 1개 묶음이니까 100 + 1
# 만약에 7 441 6 -> 2초 4초 2초 +1
import sys
input = sys.stdin.readline
n,w,l = map(int,input().split())
truck = list(map(int,input().split()))
weight = 0
cnt = 0
time = 0
over = False
for i in range(n): 
    weight += truck[i]
    cnt += 1
    if weight > l:
        weight = truck[i]    
        time  += w + (cnt-1)
        cnt = 1
        over = True
time += 1
if not over:
    time = w + n
print(time)