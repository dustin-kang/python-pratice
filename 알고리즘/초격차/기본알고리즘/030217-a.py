"""
좌표 압축
https://www.acmicpc.net/problem/18870

- 데이터가 백만 개가 주어지니 nlogN으로 풀어도 된다.
- X'i 값이 이전 좌표들의 갯수 값 (서로 다른)
- 2는 -10, -9 2개
"""

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1. 중복원소 제거
# 2. 오름차순 정렬
unique = sorted(list(set(array)))
# 3. 각 인덱스에 매핑
mapping = dict()

for i, x in enumerate(unique):
    mapping[x] = i

# 암축 수행 결과를 확인한다.
for x in array:
    print(mapping[x], end=" ")