import sys
input = sys.stdin.readline
import itertools
n = int(input())
num = list(itertools.permutations([1,2,3,4,5,6,7,8,9],3))

for _ in range(n):
    test , s , b = map(int,input().split())
    test = list(str(test))
    remove_count = 0

    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= remove_count
        for j in range(3):
            test[j] = int(test[j])
            

