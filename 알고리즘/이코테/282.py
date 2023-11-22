"""
# 다이나믹 프로그래밍 - 1로 만들기

26 -> 3

- dp[i - 1] , dp[i // 2], dp[i // 3], dp[i // 5] 중 가장 최소가 나오는 식으로 보텀업 진행
- 진행 횟수를 위해 +1을 더해준다.
"""


x = int(input())

dp_table = [0] * (x+1)

for i in range(2, x+1): # 2~ 26
    dp_table[i] = dp_table[i - 1] + 1
    if i % 2 == 0: # 2로 나누어 떨어지는 경우
        dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
    if i % 3 == 0: # 3로 나누어 떨어지는 경우
        dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
    if i % 5 == 0: # 5로 나누어 떨어지는 경우
        dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)

print(dp_table[x])
