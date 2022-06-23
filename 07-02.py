'''
있으면 yes
없으면 no

입력예시
5  보기 배열의 크기
8 3 7 9 2   보기 숫자
3  찾는 배열의 크기
5 7 9   찾는 숫지

출력예시
no yes yes
'''
import time

n = int(input())
total = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))
result=[]
start = time.time()
for i in range(m):
    result.append("no")

for i in range(m):
    for j in range(n):
        # print("total[j]: ",total[j])
        # print("find[i]: ",find[i])
        if(total[j]==find[i]): #한번 탐색을 완료하였을 때 결과를 출력하도록 해야함.
            result[i]="yes"

for i in range(m):
    print(result[i],end=" ")

print(" \n")

# 이진탐색으로 풀어보기 외우기!
def binary_research(array,target,start,end):
    while(start<=end):
        mid = (start + end) //2
        if(array[mid]==target):
            return print("yes",end=" ")
        elif(array[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return print("no",end=" ")

total.sort() #total 오름차순 정렬
for i in range(m):
    binary_research(total,find[i],0,n-1)


print(" \n time : ",time.time()-start)
