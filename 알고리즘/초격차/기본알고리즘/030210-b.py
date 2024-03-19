"""
기타리스트
중
https://www.acmicpc.net/problem/1495

마지막 곡을 연주할 수 있는 볼륨 중 최대값
"""


# 연주할 곡(N), 볼륨 리스트(V), 시작 볼륨(S), 볼룸의 최대값(M)
N, S, M = map(int, input().split())
change = list(map(int, input().split()))

V = [[False] * (M+1) for _ in range(N+1)] # 시작 전에 바꿀 수 있는 볼륨 리스트
V[0][S] = True

# 모든 볼륨에 대해 연주 가능 여부 계산하기
for i in range(N+1):
    for j in range(M+1):
        if V[i-1][j] == False:
            continue
        if j - change[i - 1] >= 0: # -볼륨 경우
            V[i][j - change[i-1]] = 1
        if j + change[i - 1] <= M: # +볼륨 경우
            V[i][j + change[i-1]] = 1

result = -1
for i in range(M, -1, -1): # 끝부터 탐색
    if V[N][i] == True: # 가장 마지막의 ROW의 가장 큰 값 True
        result = i
        break

print(result)


    

