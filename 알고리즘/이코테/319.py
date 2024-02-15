"""
DFS, BFS - 연산자 끼어넣기

수의 갯수
수열
n-1개인 연산자(덧뺼곱나)

최대값 출력
최소값 출력

2
5 6
0 0 1 0

30
30

---

3
3 4 5
1 0 1 0

35
17

---

6
1 2 3 4 5 6
2 1 1 1

54
-24
"""

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최소값, 최대값 초기화
min_value = 1e9
max_value = -1e9

def dfs(i, now):
    """
    `i` : 다음 수의 인덱스
    `now` : 초기값(첫 숫자)

    여러번의 사칙연산을 줄여 최댓값과 최솟값을 구한다.
    """
    global min_value, max_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1 
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1 
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1 
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1 

dfs(1, data[0])

print(max_value, min_value)

"""
혹은 중복 순열로 문제를 해결할 수 있다.
n이 3일때 총 16개의 식을 만들 수 있으며 이 식에서 최대값과 최소값을 찾으면 된다.
"""

from itertools import product

n = 3
print(list(product(['+','*'], repeat=(n-1)))) # 2번 예제의 경우 4개의 식이 나온다. 그중 최대, 최소 값을 찾으면 된다.