'''
4
2 1 1 0
키가 1인데 왼쪽에 큰 사람 두명 
키가 2인데 왼쪽에 큰 사람 한명  
키가 3인데 왼쪽에 큰 사람 한명  
키가 4인데 왼쪽에 큰 사람 0명  
4 2 1 3
발견 규칙:
처음 나오는 값은 1이 그 인덱스에 자리한다는 것.

모든 조합을 만들어서 일치하는 것만 볼까?
일치 조건을 만들바에 직접 구현하는게 나음.
1일 때는 2를 다 채워놓고
1을 픽스 하기.
2가 들어갈 때는 1의 자리를 제외한 곳에 3을 다 채워놓고 픽스하기
3이 들어갈 때는 1과 2의 자리를 제외한 곳에 4을 다 채워놓고 픽스하기
'''

import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
num_list = [11 for _ in range(n)]
num_reset = [0,0,0,0]
# print(num_list)
for i in range(n):
    val = num[i] #키 1,2,3,4, 순으로 val 메겨짐 
    cnt = 0
    changed = False
    for j in range(n): #0,  
        if cnt == val:
            for k in range(j,n):
                if  num_list[k] == 11 and not changed:
                    num_list[k] = (i+1)
                    # print(num_list)
                    changed = True
                             
        if num_list[j] > (i+1):
            cnt += 1
        
    #val이 2 일때 i는 0. j=0이면 cnt1. j=1이면 cnt=2 . j는 2이면 num_list[2] = 1
    #val이 1일때 i는 1. i+1 은2. j=1에 cnt1 만족 후, num
for i in range(len(num_list)):
    num_list[i] = str(num_list[i])
print(" ".join(num_list))

