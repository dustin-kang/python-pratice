"""
효율적인 화페 구성

input
2 15
2
3

input2
5

output
3 4
3
5
7

ouput2
-1
"""


# 정수 n과 m을 입력받는다.
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력 받는다.
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
memo = [10001] * (m + 1) # 0~15개의 초기 리스트 값을 구성합니다.

# 다이나믹 프로그래밍 진행 (Bottom Up)
memo[0] = 0 # 동전이 없으면 무조건 0

for i in range(n):
    for j in range(array[i], m + 1): # 2 ~ 15 # 3 ~ 15
        if memo[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            memo[j] = min(memo[j], memo[j - array[i]] + 1)

# 계산된 결과
if memo[m] == 10001: # 만약 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(memo[m]) # 15일 때 사용할 수 있는 최소 개수