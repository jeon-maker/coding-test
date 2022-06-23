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

n = int(input())
total = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))
result=[]
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