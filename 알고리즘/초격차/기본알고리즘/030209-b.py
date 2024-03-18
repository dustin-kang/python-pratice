"""
평범한 배낭
https://www.acmicpc.net/problem/12865
O(NK)
"""

n, k = map(int, input().split()) # 물품수와 최대 무게

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split()) # 현재 무게와 가치
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v) # 위에 값, 현재까지 구했던 값 + 현재 가치

print(dp[n][k])
