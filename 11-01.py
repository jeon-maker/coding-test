'''

모험가 길드

공포도 N이 주어졌을 때, N명과 함께 가야함
입력 예시
5
2 3 1 2 2

출력 예시
2
'''
#줄을 세워서 정렬시킴.
#같은 숫자끼리 묶임.
n = int(input())
arr = list(map(int,input().split()))
arr_2 = arr
arr.sort()
arr = list(set(arr)) #arr 중복 제거
# print(arr)
count = 0
for i in range(len(arr)):
    arr_b = []
    for j in range(n):
        if(arr[i]==arr_2[j]):
            arr_b.append(arr_2[j])
            # print(arr_b)
    count += len(arr_b)//arr[i] #전부 다 들어가 진 다음에서야 길이를 정령해야함
    # print(count)        
print(count)
    
