import sys
input = sys.stdin.readline
s = list(input().strip())
s.sort()
pelin = [''] * len(s)
pelin2 = [''] * len(s)
import string
upper = [i for i in string.ascii_uppercase]
possible = 0
reverse = int(len(s)-1)
if len(s) % 2 == 0 :
    #짝수 일 때
    for i in range(0,len(s),2):
        a = s[i]
        b = s[i+1]
        pelin[i] = a
        pelin2[i] = b
elif len(s) % 2 == 1:
    for x in upper:
        cnt = s.count(x)
        if cnt % 2 == 1:
            key = x
            possible += 1
    s.remove(key)
    # print("key : ",key)
    for i in range(0,len(s),2):
        a = s[i]
        b = s[i+1]
        pelin[i] = a
        pelin2[i] = b

if pelin == pelin2:
    # pelin.remove(0)
    # pelin2.remove(0)
    answer = []
    for i in range(len(pelin)):
        answer.append(str(pelin[i]))
    if possible == 1:
        answer.append(str(key))
    for i in range(len(pelin2)):
        answer.append(str(pelin2[reverse - i]))
    print("".join(answer))    
elif pelin != pelin2 or possible >1  :
    print("I'm Sorry Hansoo")