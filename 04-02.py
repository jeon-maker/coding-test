'''
정수 N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 
작성하시오
예를들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
00시 00분 03초
00시 13분 30초
반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.
00시 02분 55초
01시 27분 45초

입력조건 : 첫째줄에 정수 N이 입력된다 (0<=N<=23)
출력조건 : 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를
출력한다
입력예시 5
출력예시 11475

'''

n = int(input(""))
Time , Minute , Count = 0,0,0
mycount = 0 # 3이 들어가는 횟수


for t in range(n+1):
    print(Time)
    if(Time==3 or Time==13 or Time==23):
        mycount += 60*60
    else: #중복되지 않을때
        for i in range(60):
            Minute += 1
            if(Minute==3 or Minute==13 or Minute==23 or 29<Minute<40 or Minute==43 or Minute==53): #or 연산자는 bool 타입 연산자이기 때문에, 타입을 비교한다
                mycount += 60
            else: #중복되지 않을 때.
                for j in range(60): 
                    Count += 1
                    if(Count==3 or Count==13 or Count==23 or 29<Count<40 or Count==43 or Count==53):
                        mycount +=1
            Count=0 #초는 0으로 다시 초기화
    Minute = 0 #시간도 다시 0으로 초기화
    Time += 1
print(mycount)

##답안 
h= int(input())
count_= 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k): #매 시각 안에 '3'이 포함되어 있다면 카운트 증가.
                count_ +=1
print(count_)
