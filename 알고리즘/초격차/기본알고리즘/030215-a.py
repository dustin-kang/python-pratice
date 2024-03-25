"""
센서
https://www.acmicpc.net/problem/2212
"""

# 각 집중국의 수신 가능영역의 거리의 합의 최소화
# 각 센서 사이의 거리를 구하고 가장 거리가 먼 순서대로 끊어버림
"""

- - - - - - - - -
1   3     6 7   9 <- 센서
  2    3   1  2   <- 거리 차이

1, 3 // 6, 7, 9로 k 만큼 끊어버림

- - - -|- - - - -
1   3  |  6 7   9 <- 센서
  2    |   1  2   <- 거리 차이

그럼 합은 5가 됨.
"""

import sys

n, k = int(input()), int(input()) # 센서(n)와 집중국(k)

if k > n: # 센서보다 기지국이 많은 경우(흑자..)
    print(0)
    sys.exit()

array = list(map(int, input().split())) # 좌표
array.sort() # 오름차순 정렬

distance = []
for i in range(1, n):
    distance.append(array[i] - array[i - 1])
distance.sort(reverse=True) # 가장 거리가 큰 것 부터 계산을 위해 내림차순 정렬

for i in range(k-1): # 기지국 수 만큼 끈어버림
    distance[i] = 0

print(sum(distance))







