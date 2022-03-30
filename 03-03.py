#숫자 카드 게임
#숫자가 쓰인 카드들이 N * M 형태로 놓여있다.
#N은 행의 개수 M은 열의 개수
#먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
#그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
#따라서 처음에 카드를 골라날 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를
#뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다

# 내 답안
n,m = map(int,input().split())
#n개의 배열을 만들어서 각 배열당 m개의 원소가 들어가게 하자.
min_list = []
for i in range(n):
    data = list(map(int,input().split()))
    ####리스트로 입력 받기 기억 할 것.
    data.sort()
    min_val = data[0] # 가장 작은 값 넣기
    min_list.append(min_val)

min_list.sort()
print(min_list[-1])   


# 답지 풀이
#min_value = min(data) # 가장 작은 값을 찾는 것을 이용
#result = max(result,min_value) #범위에서 가장 큰 값 찾는 방법    


