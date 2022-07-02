'''볼링공 고르기
입력 예시
5 3
1 3 2 3 2
출력예시 
8

입력예시
8 5
1 5 4 3 2 4 5 2
출력예시
25

'''

n,m = map(int,input().split())
ball = list(map(int,input().split()))
cnt = 0
def choice(arr):
    global cnt
    L = len(arr)
    for i in range(L):
        for j in range(L):
            if ((i <= j) and (arr[i] != arr[j])):
                cnt +=1
            else:
                pass

choice(ball)
print(cnt)