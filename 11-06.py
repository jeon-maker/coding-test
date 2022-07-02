food_times = list(map(int,input().split()))
k = int(input())
num = 0
def solution(arr,k):
    global num
    length = len(arr)
    for i in range(k):
        j = i % length
        if(arr[j]==0):
            j = j+1
            arr[j] = arr[j]-1
        else:
            arr[j] = arr[j]-1
        if(j==0):
            num = 2
        elif(j==1):
            num = 3
        elif(j==2):
            num = 1
        
        print("j : ",j, " food_times : ",arr)
    return(num)
answer = solution(food_times,k)
print(answer)
        
