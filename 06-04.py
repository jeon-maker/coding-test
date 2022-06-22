'''
두 배열의 원소 교체

입력 예시
5 3 ( 5는 배열의 크기 3은 바꿀수 있는 최대 횟수)
1 2 5 4 3
5 5 6 6 5

출력예시 26
'''

from re import A


n,m = map(int,input().split())
arr_A = []
arr_B = []

arr_A = (list(input().split()))
arr_B = (list(input().split()))
for i in range(n):
    arr_A[i]=int(arr_A[i])
    arr_B[i]=int(arr_B[i])
arr_A.sort(reverse=True) #오름차순 정렬
arr_B.sort(reverse=True) #오름차순 정렬

print(arr_A)
print(arr_B)
#최대 k번 바꿔치기를 할 수 있는데, 만약 A에서 가장 작은 원소가 B의 가장 큰 원소보다 크다면 멈춰야함

for i in range(m):
     if(arr_A[n-1-i]<arr_B[i]):
        arr_A[n-1-i],arr_B[i] = arr_B[i],arr_A[n-1-i]
print(arr_A)
print(arr_B)
hap = 0
for i in range(n):
    hap += int(arr_A[i])

print(hap)
