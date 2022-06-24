'''
떡볶이 떡 만들기.
떡 절단기의 최대 높이 설정하기.

입력예시
4 6 (4는 떡 갯수 6은 주문한 떡의 길이. 절단기로 다 넣어버림.)
19 15 10 17

출력예시 (절단기 최대높이)
15

숫자 범위가 크기 때문에 이진 탐색을 쓰는게 좋을 듯.
제일 긴 떡의 길이를 end로 잡고 이진탐색 하기.

'''
n,m = map(int,input().split())
before_cut=list(map(int,input().split()))
before_cut.sort()
# 
def binary_search(array,start,end,target):
    
    while(start<=end): #mid의 최대를 찾아줌 자동으로.
        mid = (start+end)//2 # start 와 end를 제일 짧은 떡의 길이 , 제일 긴 떡의 길이로 설정해주기
        x=0
        for i in range(len(array)):
             if(array[i]-mid>0):
                 x +=array[i]-mid
        if(x==target):
            return print(mid)
        elif(x<target): #떡이 더 길게 짤릴 경우 start를 더 
            end = mid-1 
        elif(x>target):
            start = mid+1
binary_search(before_cut,before_cut[0],before_cut[n-1],6)
        