'''
번호순으로 책 정렬하기.

1이 맨 앞에 있다면
맨 뒤에 있는 숫자보다 하나 큰게 계속 뒤로 오면 됨.
예를들어


15423이면 
15234
12345

14523
15234
12345



21453
21534
21345
23451
음..

21453
14532
14523
15234
12345

1이 맨 앞에 없다면?

321
312
123

뒤집어진 것 중 작은것을 뒤로 보낸다?
'''
import sys
input = sys.stdin.readline
n = int(input())
book = [int(input()) for _ in range(n)]
print(book)
ans = sorted(book)
print(ans)

cnt = 0
while True:
    back = 300001
    if ans == book:
        break
    for i in range(n-1):
        a = book[i]
        # print(a)
        b = book[i+1]
        # print(b)
        if a > b:
            back = min(a,back)
            # print("back is ")
            # print(back)
    book.remove(back)
    book.append(back)
    print(book)
    cnt += 1
print(cnt)