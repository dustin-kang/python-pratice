"""
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
"""

n = int(input())

dp = [1] * n # 모든 원소의 길이는 각 1
array = list(map(int, input().split()))
max_num = array[0]

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]: # i가 더 크다면 반복적으로 갱신해나감
            dp[i] = max(dp[i], dp[j] + 1)
            

print(max(dp))