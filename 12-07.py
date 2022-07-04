'''
짝수 자릿수의 입력이 들어올 때,
반을 나누어 왼쪽의 숫자들의 합과 오른쪽의 숫자들의 합이 같아야함.
배열을 만들어서 두개로 쪼개고 합을 구하면 될듯?
'''
from turtle import right


n = str(input())
score = []
length = len(n)
for i in range(length):
    score.append(int(n[i]))
half = int(length/2)

left_hap = 0
right_hap = 0
for i in range(half):
    left_hap += score[i]
    right_hap += score[-(i+1)]
if(left_hap == right_hap):
    print("LUCKY")
else:
    print("READY")
