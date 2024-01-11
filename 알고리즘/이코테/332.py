"""
다이나믹 프로그래밍 - 정수 삼각형

5
7
3 8
8 1 0
2 7 4 4 
4 5 2 6 5

30
"""

n = int(input())
dp = []
# dp[0] = int(input())

# for i in range(1, n):
#     array = list(map(int, input().split()))
#     dp[i] = max(array[i-1]+dp[i-1], array[i]+dp[i-1])

# print(dp[n-1])

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n): # 열
    for j in range(i+1): # 원소의 인덱스
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == 1:
            up = 0
        else:
            up = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))