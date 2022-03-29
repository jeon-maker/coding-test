#큰수의 법칙
#배열의 크기 N . 더해지는 횟수 M . 그리고 k (연속 더하기 가능 횟수)
#입력 조건
#첫째줄에 N(2<=N=1000) M(1<=M<=10000) K (1<=k<=10000)의 자연수가 주어지며
#각 자연수는 공백으로 구분한다
#둘째줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다
#단 각각의 자연수는 1이상 10000이하의 수로 주어진다.
#입력으로 주어지는 K는 항상 M보다 작거나 같다.

#출력 조건 : 첫째줄에 동빈이의 큰 수의 법칙에 따라 답을 출력한다

#입력예시 
#5 8 3
#2 4 5 4 6
#출력예시
#46

#나의 답안
n,m,k=map(int,input().split()) #한줄 입력받기
data =list(map(int,input().split())) #n개의 수 입력 받기
data.sort() # 수 정렬하기

first = data[n-1] #가장 큰 수
second = data[n-2] #두번째 큰 수

hap = 0

first_times = (m//(k+1))*k + (m%(k+1))
second_times = (m - (first_times))
hap = (first*first_times) + (second*second_times)
print(hap)

#출력 결과는 맞았지만 논리에 오류가 있음
#수정 완료
#first times , second times  잘 생각해보기









