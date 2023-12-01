"""
다이나믹 프로그래밍 - 효율적인 화폐 구성
최소한의 화폐 개수로 합이 M이 되도록 만든다. 대신 몇개라도 사용할 수 있다. 그럼 몇개의 화폐가 필요한가
불가능할 땐 -1을 리턴하자. (1 <= N <=100, 1 <= m <= 10000)
- 화폐의 단위 갯수 , m원
- 화폐 단위들...

2 15
2
3

-> 5

3 4
3
5
7

-> -1
"""

n, m = map(int, input().split())

array = [int(input()) for _ in range(n)]

dp = [10001] * (m+1)
dp[0] = 0 # 초기값

for i in range(n): # 화폐(0(2),1(3))마다 인덱스(값)
    for j in range(array[i], m+1): # 2~ 15 : 15까지의 몇개의 경우의 수가 있는지 확인
        # if dp[j - array[i]] != 10001: # dp[2-2]  / dp[3-2] / dp[4-2]
        dp[j] = min(dp[j], dp[j - array[i]]+1) # dp[2] = 1 / X / dp[4] = 2

if dp[m]  == 10001: # 만약 만들 수 없는 경우라면 -1 리턴
    print(-1)
else:
    print(dp[m])
