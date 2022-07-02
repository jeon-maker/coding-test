food_times = list(map(int,input().split()))
k = int(input())
num = 0

def find(arr,p):
    length = len(arr)
    if(arr[p]==0):
        while(arr[o]==0):
            for i in range(length):
                o = i
            if(arr[o]!=0):
                break
    return o



def solution(arr,k):
    global num
    length = len(arr)
    for i in range(k):
        j = i % length # j는 현재 0 1 2 - 0 1 2 - 순으로 돌아감.
        if(arr[j]==0):
            j = find(arr,j)
            arr[j] = arr[j]-1
        else:
            arr[j] = arr[j]-1
        num = j+2
        if(num > length):
            num = num % length

        
        print("j : ",j, " food_times : ",arr)
    return(num)
answer = solution(food_times,k)
print(answer)
        
