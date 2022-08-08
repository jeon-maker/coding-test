'''
모든 숫자를 알고 있어야함.
제일 높은것에서 팔도록 하기.
max를 찍으면 차이를 기록하고 그 차이에 합을 더함.. 다시 맥스 리셋..
안될듯.
가장 높은거 전까지 차이 다 팔고 -> 팔면 다시 리셋을 해야하는게 문제.
가장 높은것의 인덱스를 찾아서, 합을 다 하고 인덱스를 지워버리기.
두번째는 그 후로 안팔린거 팔고
세번째 그 후로 안팔린거 팔고
'''
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    days = int(input())
    price = list(input().split())
    for i in range(days):
        price[i] = int(price[i])
    income = 0
    val = 0
    for i in range(days-1,-1,-1):
        val = max(val,price[i])
        if price[i] != val:
            income += val - price[i]
    print(income)