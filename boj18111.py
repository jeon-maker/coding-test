import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
ans = sys.maxsize
for target in range(257):
    max,min = 0,0
    for i in range(n):
        for j in range(m):
            if ground[i][j] < target :
                min += target - ground[i][j]
            else :
                max += ground[i][j] - target
            
    inventory = max + b
    if inventory < min:
        time = 2*max + min
        if time <= ans:
            ans = time
            idx = target
print(ans,idx)


# '''
# 1.총합의 평균을 낸다
# 2.설치된 것의 평균을 낸다
# 내림을 한다 
# 만약에  0 0 0 100 이면?
# 나눠주는게 더 빠름
# '''

# hap = 0
# for i in range(n):
#     for j in range(m):
#         hap += ground[i][j]

# total = hap + b
# total_aver = total//(n*m)
# aver = hap//(n*m)

# #way 1 총합 평균에 맞추기
# count_1 = 0
# count_2 = 0
# for i in range(n):
#     for j in range(m):
#         miss = total_aver - ground[i][j]
#         miss_2 = aver - ground[i][j]
#         if miss<0:
#              count_1 += 2 * abs(miss)
#         else :
#             count_1 += abs(miss)
#         if miss_2<0:
#             count_2 += 2 * abs(miss_2)
#         else :
#             count_2 += abs(miss_2)
# arr = []
# if total_aver > 256:
#     count_1 = 100000
# if aver > 256 :
#     count_2 = 100000
# arr.append((count_1,total_aver))
# arr.append((count_2,aver))
# arr.sort()
# if arr[0][0] == arr[1][0]:
#     arr[0] = arr[1]
# answer= ""
# answer += str(arr[0][0])
# answer += " "
# answer += str(arr[0][1])
# print(arr)
# print(answer)