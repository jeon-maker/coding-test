'''
안될것같음.
stack으로 쌓아두고
큰 여는 괄호가 나오면 3을 스택에 쌓고
작은 여는 괄호가 나오면 2를 스택에 쌓는다.
그런데 스택 위에 다른 숫자가 들어오는 순간 그 아래 스택에 * 를 붙여준다.
스택 위에 어떠한 숫자도 들어오지 않을 경우 스택이 빠져나갈때 + 를 붙인다.

올바른 괄호인지 아닌지 검사를 하는 과정을 거친 후에 -> 위에 설명한대로 값을 계산하는 함수를 만든다 
'''

import re
import sys
input = sys.stdin.readline
braket = list(input().strip())
check_list = []
def isitcorrect(braket):
    for i in range(len(braket)):
        if braket[i] == '[':
            check_list.append('[')
        elif braket[i] == '(':
            check_list.append('(')
        elif braket[i] == ']':
            if len(check_list) == 0:
                return False
            else:
                if check_list[-1] == '[':
                    check_list.pop()
                else :
                    # print("wrong braket")
                    return False
        elif braket[i] == ')':
            if len(check_list) == 0:
                return False
            else:
                if check_list[-1] == '(':
                    check_list.pop()
                else:
                    # print("wrong braket")
                    return False
    if len(check_list) == 0:
        # print("success")
        return True
    else :
        # print("wrong")
        return False
# isitcorrect(braket)

#올바른 괄호열인지 검증하는거 성공함

cal = []
def calculate_braket(braket):
    val = 0

    for i in range(len(braket)):
        if braket[i] == '[':
            if len(cal) == 0:
                cal.append('3')
            else:
                if cal[-1]== '3':
                    cal[-1] = '3*'
                    cal.append('3')
                elif cal[-1] == '2':
                    cal[-1] = '2*'
                    cal.append('3')
        elif braket[i] == '(':
            if len(cal) == 0:
                cal.append('2')
            else:
                if cal[-1]== '3':
                    cal[-1] = '3*'
                    cal.append('2')
                elif cal[-1] == '2':
                    cal[-1] = '2*'
                    cal.append('2')
        elif braket[i] == ']' or braket[i] == ')':
            k = cal.pop()
            if k =='3*':
                val *= 3
            elif k =='3':
                val += 3
            elif k =='2*':
                val *=2
            elif k == '2':
                val += 2
    print(val)
            
if(isitcorrect(braket)):
    calculate_braket(braket)  
else:
    print("0")         


