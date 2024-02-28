"""
피보나치 수열
https://www.acmicpc.net/problem/2747
"""


# 시간 초과를 받는 실패 코드 → 재귀적 구현의 한계(반복적인 함수가 생김)
# 2^N
n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n))


# 반복문으로 문제를 해결하는 코드

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)
