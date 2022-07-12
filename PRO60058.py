w = str(input())
V = []

V_ = [] #임시 V
def solution(p):
    w_ = []
    U_ = [] #임시 U
    V = ''
    U = ''
    if not p:
        return ' '
    Open = [] # ' ( '  넣기  
    Close = [] # ' ) ' 넣기
    for i in range(len(p)):
        w_.append(p[i])
        i = 0
    print("w_ : ",w_)
    while w_: #w_가 존재하는 동안
        if w_[0] == '(':
            i += 1
            Open.append((w_[0],i))
            w_.pop(0)
        elif w_[0] == ')':
            i += 1
            Close.append((w_[0],i))
            w_.pop(0)
        if len(Open) == len(Close): #갯수가 일치할 때 바로 종료하고  #남은것은 V에 넣어야함
            for i in range(len(w_)):
                V += w_[i] #V를 문자열로 만들어야 함.
            print(" V : ",V)
            break
    # print("open : ", Open)
    # print("close : ", Close)
    for i in range(len(Open)):
        U_.append(Open[i])
        U_.append(Close[i])
    U_.sort(key = lambda x : x[1])
    for i in range(len(U_)):
        U += U_[i][0]
    print(" U : ",U)
    hap = 0
    err = 0 # 에러가 0 이면 성공, 에러가 1이면 실패
    for i in range (len(U)):
        if U[i]=='(':
            hap += 1
        else :
            hap -= 1
        if hap < 0 :
            err = 1           
            break
   # U 담기성공. 이제 올바른지 아닌지를 판단해보자 err 0 이면 올바름 err 1이면 올바르지 못함
    if err == 0 :  # 올바를 경우
        print("err 0 ")
        return U +solution(V)
        # for i in range(len(U)):
        #     answer += + U[i]
    elif err == 1 :
        answer  = '(' 
        answer += solution(V)
        answer += ')'
        print("err = 1 answer : ",answer)
        for i in range(1,len(U)-1): #3개면 0 1 2 인데 이건 1 2, ->       
            if U[i] == ')':
                answer +='('
            else :
                answer +=')'
        answer = answer.replace(" ","")
        return answer
print(solution(w))