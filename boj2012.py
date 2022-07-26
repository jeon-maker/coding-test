import sys
input = sys.stdin.readline
n = int(input())
pred = [int(input()) for _ in range(n)]
num = [int(i+1) for i in range(n)]
pred.sort()
num.sort()
hap = 0
for i in range(n):
    hap += abs(pred[i] - num[i])
print(hap)