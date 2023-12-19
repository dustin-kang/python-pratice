"""
다이나믹 프로그래밍 - 퇴사
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""

n = int(input())
lst = [list(map(int, input().split())) for i in range(n) ]
dp = [0] * (n+1)
max_value = 0

for i in range(n-1, -1, -1):
    time = lst[i][0] + i
    # 상담 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(lst[i][1] + dp[time], max_value) # 해당 날짜부터 time까지 의 합이 큰지 현재 max_value이 큰지 확인
        max_value = dp[i] # 최고 이익 계산 15 -> 35 -> 45 -> 45 -> 45
    else:
        dp[i] = max_value

print(max_value)


