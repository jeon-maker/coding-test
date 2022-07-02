'''
만들수 없는 정수
입력 예시 
5
3 2 1 1 9
출력 예시
8
'''
#접근 방법
'''
어떻게 구현할까..
1.배열을 만들고 정렬
2.작은 숫자부터 더해가기 (모든 경우의 수를 어떻게 구현할 것인가?)

모든 경우의 수를 만들어야함.
원소가 1~N개.. 반복문으로 가능한데. 반복문 N개를 어떻게 만들지?
'''

n = int(input())
data = list(map(int,input().split))
data.sort()

target = 1
for x in data:
    #만들 수 없는 금액을 찾았을 때 반복 정료
    if target < x:
        break
    target += x
print(target)