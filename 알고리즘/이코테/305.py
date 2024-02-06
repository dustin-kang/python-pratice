"""
그리디 - 볼링공 고르기

두 사람이 공을 고르는 경우의 수를 구하여라.

1 <= N <- 1,000
1 <= M <= 10
1 <= K <= M

5 3
1 3 2 3 2

8

8 5
1 5 4 3 2 4 5 2

25
"""
from itertools import combinations

n,m = map(int, input().split())
balls = list(map(int, input().split()))

# 초기 답안 #
result = []
selects = combinations(balls,2)
for select in selects:
    if select[0] != select[1]:
        result.append(select)

print(len(result))

# 모범 답안 #
array  = [0] * 11 # 총 무게는 10까지였음.
for x in balls:
    # 각 무개 별 볼링공 갯수 카운팅
    array[x] += 1
print(array)

result = 0
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공 개수 제외(A가 선택할 수 있는 개수)
    result += array[i] * n  # B가 선택하는 경우와 곱하기

"""
이 문제는 A가 특정 무게를 선택했을 때 B가 무게를 택하는 경우를 차례대로 계산하는 방식이다.

첫번째 예제의 Array  : [0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0]
두번쨰 예제의 Array  : [0, 1, 2, 1, 2, 2, 0, 0, 0, 0, 0]
"""