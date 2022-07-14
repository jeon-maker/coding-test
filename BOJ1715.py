from queue import PriorityQueue
que = PriorityQueue()
n = int(input())
after_card = []
for i in range(n):
    size = 0
    size = int(input())
    que.put(size)

hap = 0
for i in range(n-1): #
    if(que.qsize()==1):
        break
    a= que.get()
    b= que.get()
    hap += a+b #앞 두개 꺼내오기
    que.put(a+b)
print(hap)
