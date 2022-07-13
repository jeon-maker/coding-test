import sys
n= int(sys.stdin.readline())
stages = list(map(int,input().split()))
def solution(N,stages):
    results = [1]* (N+1)
    answer =[ ]

    total = len(stages)     #남은 사람 수
    for i in range(1,N+1):
        fail_total = 0 #실패 수
        fail_percent = 0 #실패율
        for j in range(len(stages)):
            if stages[j] == i:
                fail_total  += 1  #일치하면 실패 수 추가시키기
                fail_percent = fail_total / total
        total = total - fail_total

        results[i] = fail_percent # results 에는 실패율이 들어가있음. ex { 3, 4 ,1 ,7}  -> 4단계 실패율이 젤 높음 ->index를 추출해야함.
    print(results) #results에 집어넣기까지 성공.
    answer = sorted(range(len(results)),key=lambda k : results[k], reverse=True)
    answer.pop(0)
    print(answer) #results에 집어넣기까지 성공.

    return answer

solution(n,stages)