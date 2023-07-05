"""
볼링공 고르기

<문제 해석>
볼링공 N개, 최대 무게 M, 각 공 무게가 1, 3, 2, 3, 2이라 할 때 두 사람이 고를 수 있는 공의 조합을  구하여라
다만 두 사람은 서로 다른 무게의 공을 들어야한다.


<입력>
5 3
1 3 2 3 2

<입력 2>
8 5
1 5 4 3 2 4 5 2

<출력>
8

<출력 2>
25
"""

# 문제 풀이 1
n,m = map(int, input().split())
lst = list(map(int, input().split()))
from itertools import combinations
a = len(lst) - len(set(lst))
print(len(list(combinations(lst, 2))) -a)

# 문제 풀이 2
# 이 문제를 풀 때에는 A가 무게를 들었을 떄 B가  선택하는 경우의 수를 구하면 된다.
# 무게가 낮은 공부터 높은 공까지 하나하나 순서대로 확인한다.
# 만약 A가 1인 무게를 택했을 때, B는 2,3,4,5번쨰 공을 선택할 수 있다.
# A가 2인 무게를 택했을 때, B는 2, 5번째 공을 선택할 수 있다.
# 3일 떄는 고를 수 없다.

# 1 ~ 10까지
array = [0] * 11
for x in lst:
    array[x] += 1

result = 0
# 1부터 m(최대 무게)까지 처리
for i in  range(1, m+1):
    n -= array[i] # 무게가 i인 공의 개수 제외
    result += array[i] * n # B가 선택한 공의 개수와 곱하기
    

