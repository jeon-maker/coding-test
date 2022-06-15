def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("재귀적으로 구현 :  " ,factorial_recursive(5))


#유클리드 호제법
'''
두 자연수의 최대공약수를 구하는 것

예시 GCD(192,162)

1단계 192 162의 나머지 =30
=> 2단계 162와 30
=> 3단계 12와 30
=> 4단계 12와 6


재귀적으로 호출하면 메모리 내부의 스택 프레임에 쌓임.

'''

'''
DFS 깊이 우선 탐색

'''