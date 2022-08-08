'''
그래프 이용?

1. 뒤에 +1

2. 값 * 2

매번 선택해서 값이 도출되면 cnt 세기?

'''
import sys
input = sys.stdin.readline
from collections import deque
a,b = map(int,input().split())
q= deque()
q.append((a,1))

while(q):
    n,t = q.popleft()
    if n < b :
        continue
    if n == b:
        print(t)
        break
    q.append((int(str(n)+"1"),t+1))
    q.append((n*2,t+1))
else:
    print(-1)