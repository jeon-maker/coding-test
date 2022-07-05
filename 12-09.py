def solution(s):
    answer = 0
    box = []
    check_length = int(len(s)/2) # 내림하게 됨. 입력받은 문자열 길이의 반토막
    for i in range(1,check_length+1):
        check = list_chunk(s,i) #분할된 것.
        print(i, check)
    return answer
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
solution('abcabcabc')