import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
que = PriorityQueue()
aver = 0
mid = 0
freq = 0
bound = 0
num = [ ]# 최빈값 구하는 용도
for i in range(n):
    que.put(int(input()))
hap = 0
for i in range(n):
    a = que.get()
    hap += a
    num.append(a)
num.sort()
from collections import Counter
cnt = Counter(num)
cnt = cnt.most_common()
frequency = cnt[0][1]
most__ = []

for k in cnt:
    if k[1]==frequency:
        most__.append(k[0])
# print(len(most__))
if len(most__)==1:
    freq = most__[0]
elif len(most__) != 1:
    freq = most__[1]

aver = round(hap/n)
mid = num[int((n-1)/2)]
MIN = num[0]
MAX = num[n-1]
bound = MAX - MIN
print(aver)
print(mid)
print(freq)
print(bound)