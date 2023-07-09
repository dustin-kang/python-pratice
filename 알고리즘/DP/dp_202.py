"""
개미 전사

-input-
4
1 3 1 5

-output
8
"""

memo = [0] * 100

n = int(input())

array = list(map(int, input().split()))

# 다이나믹 프로그래밍 진행 (보텀업)
memo[0] = array[0]
memo[1] = max(array[0], array[1])
for i in range(2, n):
    memo[i] = max(memo[i-1], memo[i-2] + array[i])
print(memo[n-1])
