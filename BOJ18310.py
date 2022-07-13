n = int(input())
home = list(map(int,input().split()))
choice = []
# for i in range(len(home)):
#     hap = 0
#     standard = home[i]
    
#     for j in range(len(home)):
#         # print(abs(standard-home[j]))
#         hap += abs(standard-home[j])
#     # print("standard : ",standard)
#     # print(hap,i)
#     choice.append((hap,i))
# choice.sort()
# print(home[choice[0][1]])


home.sort()
#시간제한이 뜨니까 중간값만 출력하면 됨.
# 3개 일 땐 1번 출력하면 됨. 3//2 --> 2//2
# 4개 일 땐  0번이나  1번 출력 4//2 --> 3//2 1
# 5개 일 땐 2번 출력 4//2
mid = (len(home)-1)//2 
print(home[mid])