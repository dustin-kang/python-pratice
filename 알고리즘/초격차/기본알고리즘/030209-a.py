"""
01타일
https://www.acmicpc.net/problem/1904
"""
# "00", "1"만 존재하는 타일
n = int(input())

dp = [0] * 1000001
dp[1] = 1 # 1개일 때 만들 수 있는 갯수
dp[2] = 2 # 2개일 때 만들 수 있는 갯수

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])