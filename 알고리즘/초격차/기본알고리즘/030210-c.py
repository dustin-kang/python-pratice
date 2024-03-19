"""
가장 높은 탑 쌓기
상(HARD)
https://www.acmicpc.net/problem/2655
"""

n = int(input()) # 벽돌의 수(최대 100개)

bricks = []

for i in range(n):
    # 벽돌 정보 : 너비, 높이, 무게 (10,000 보다 작거나 같음)
    w, h, k = map(int, input().split())
    bricks.append((i+1, w, h, k))

bricks.append((0,0,0,0))

# 밑면은 달라야하지만 높이는 같을 수 있다.
# 밑면이 넓은 벽돌위에 밑면이 좁은 벽돌을 올려야 한다. 넓은 돌이 아래
# 무게가 무거운 벽돌 위에 무게가 가벼운 벽돌을 올려야 한다. 무거운 돌이 아래

bricks.sort(key= lambda x : x[3]) # 무게를 기준으로 정렬
# print(bricks)

# 벽돌의 너비가 더 넓은 경우 높이를 갱신(dp)
# 이전 벽돌(i-1) 위에 쌓을 수 있는지 확인

dp = [0] * (n + 1) # 벽돌 갯수 만큼

for i in range(1, n+1):
    for j in range(0, i):
        if bricks[i][1] > bricks[j][1]: # 현재 보고 있는 벽돌의 너비가 더 넓은 경우
            dp[i] = max(dp[i], dp[j] + bricks[i][2]) # 더 큰 방향으로 테이블 갱신


# 역추적
# 가장 높이가 높을 때에서 가감!
            
print(dp)
max_value = max(dp) # 가장 큰 높이의
index = n # 인덱스
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(bricks[index][0])
        max_value -= bricks[index][2] # 가장 아래에 있어야할 벽돌의 높이부터 가감
    index -= 1

result.reverse()
print(len(result)) # 사용한 벽돌의 수
[print(i) for i in result] # 위부터 아래까지의 벽돌