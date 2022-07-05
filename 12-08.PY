#문자열 재정렬
num = ['0','1','2','3','4','5','6','7','8','9']
num_= []
str_= []
S = list(str(input()))
print(len(S))
for i in S:
    print(i)
    if i in num:
        print("number",i)
        num_.append(int(i))
        print("removed : " , i)
        print("after remove S : " , S)
    else:
        print("str",i)
        str_.append(i)
hap = 0

for i in num_:
    hap += i
str_.sort()
str_.append(hap)
for i in str_:
    print(i,end="")
