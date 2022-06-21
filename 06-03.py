from numpy import array


n = int(input())
arr=[]
for i in range(n):
    arr.append(list(input( ).split()))
'''
#선택 정렬하기
for i in range(len(arr)):
   min_index = i
   for j in range(i+1,len(arr)):
    if(arr[min_index][1]>arr[j][1]):
        min_index = j
    arr[i],arr[min_index] = arr[min_index], arr[i] #스와프

for i in range(len(arr)):
    print(arr[i][0],end=" ")'''

arr = sorted(arr, key=lambda x:x[1])
for i in arr:
    print(i[0],end=" ")