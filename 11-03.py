'''
문자열 뒤집기
'''



#부분을 뒤집을 수 있고, 전체를 뒤집을 수 있음.
# 연속된 묶음을 파악해야함. 즉 연속적인 숫자는 의미가 없음.
# 축소된 모형이 01010 이면 1을 바꾸는거 두번하면 됨.
num = list(str(input().split()))

def make_mini(arr):
    mini = []
    for i in range(len(num)-1):
        if(arr[i]!=arr[i+1]):
            mini.append(arr[i]) #전에꺼만 넣자?!
    mini.append(len(arr)-1) #마지막 것도 넣어서 빠지는 값 없게 해주자
    return mini    
        
def count0or1(arr):
    cnt0 = arr.count(0)
    cnt1 = arr.count(1)
    return(min(cnt0,cnt1))
print(make_mini(num))
print(count0or1(make_mini(num)))

