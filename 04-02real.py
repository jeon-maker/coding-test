#8 * 8 체스판
#왕실의 나이트는 다음과 같은 2가지 경우로 이동할 수 있다.
#수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
#수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
#8*8 좌표평면에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성하시오
#입력조건 : 첫째 줄에 8*8 좌표 평면상에서 현재 나이트가 위치한 곳의 자표를 나타내는 두 문자로 구성된
#문자열이 입렫된다. 입력문자는 a1처럼 열과 행으로 이뤄진다.
#출력조건 : 첫째줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.

#입력 예시 : a1           출력 예시 : 2

#수평2 수직1 -> a,b 는 오른쪽으로만 이동 g,h는 왼쪽으로만 이동 ,,, 1은 밑으로만 8은 위로만
#수직2 수평1 -> a는 오른쪽으로만 이동 h는 왼쪽으로만 이동 1,2 는 밑으로만 이동 7,8은 위로만 이동
#case를 나눠서 계산후에 합치자.

where = str(input())
garo = where[0]
sero = where[1]
garo2 = where[0]
sero2 = where[1]
total = 0 # 총합
caseA = 0 #수평2 수직 1
caseB = 0 #수직2 수평 1

#case A
if (garo=='a' or garo=='b' or garo=='g' or garo =='h'):
    if(sero=='1' or sero=='8'):
        caseA = 1
    else:
        caseA = 2
else:
    if(sero=='1' or sero=='8'):
        caseA = 2
    else:
        caseA = 4

#case B
if(sero2 == '1' or sero2 =='2' or sero2=='7' or sero2=='8'):
    if(garo2=='a' or garo2=='h'):
        caseB = 1
    else:
        caseB = 2
else:
    if(garo2=='a' or garo2=='h'):
        caseB = 2
    else:
        caseB = 4
total = caseA + caseB
print(total)



    

