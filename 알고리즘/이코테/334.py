"""
병사 배치하기
https://www.acmicpc.net/problem/18353
"""

n = int(input())
lst = list(map(int, input().split()))
lst.reverse() # 감소하는 가장 긴 수열을 위해 뒤집기

dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
  for j in range(0, i):
    if lst[j] < lst[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) # 열외