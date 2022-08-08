'''
A - ( B + C ) 일때 최소
- 뒤로 + 나올 때 까지 묶기
A - B + C - D 면
B+C 먼저해서
A- (B+c) - D

'''
import sys
input = sys.stdin.readline
equation = list(input().split("-"))
braket = []
for i in range(len(equation)):
    plus = []
    hap = 0
    if "+" in equation[i]: 
        plus = list((equation[i].split("+")))
        for j in range(len(plus)):
            hap += int(plus[j])
        equation[i] = hap
ans = int(equation[0])
for i in range(1,len(equation)):
    ans -= int(equation[i])
print(ans)    

