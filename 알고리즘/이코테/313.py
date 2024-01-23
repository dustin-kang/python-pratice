"""
치킨 배달
https://www.acmicpc.net/problem/15686

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5
"""

from itertools import combinations

n,m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1: # 해당 좌표가 집(1)인 경우
            house.append((r,c))
        elif data[c] == 2: # 해당 좌표가 치킨집(2)인 경우
            chicken.append((r, c)) # row, column

candidates =  list(combinations(chicken, m)) # 모든 치킨집 중 m개의 치킨집을 뽑는 조합
# [((1, 2), (2, 2), (4, 4))] 이번예제는 경우가 하나임

def get_sum(candidate):
    """
    치킨 거리의 합을 계산하는 함수
    |r1 - r2| + |c1 - c2|
    """
    result = 0
    for hx, hy in house:
        temp = 1e9 # 무한대로 초기값
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

# 치킨 거리의 합을 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)