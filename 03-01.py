# Created on 전성철의 iPad.
# 당장 좋은 것만 선택하는 그리디

#거스름돈 예제
#당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원,
# 100원, 50원 , 10원 짜리 동전이 무한히 존재한다고 할 때, 손님에게 거슬러 줘야
#할 돈이 N원 일 때, 거슬러 줘야 할 동전의 최소 개수를 구하라.
#(단 거슬러 줘야 할 돈 N은 항상 10의 배수이다)

# 내 답
n = int(input("거스름돈 : "))
coins = [ 500 , 100 , 50 ,10]
hap = 0 #동전의 개수
for i in coins:
    changes = n//i
    n %= i
    hap += changes
    print ("changes : " , changes )
print(hap)    

#책의 답
n = int(input("거스름돈:"))
count = 0
coin_types=[500,100,50,10]
for coin in coins:
    count += n//coin
    n%=coin
print(count)    
