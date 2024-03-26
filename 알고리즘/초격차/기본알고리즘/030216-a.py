"""
N-Queen
중
https://www.acmicpc.net/problem/9663

퀸은 대각선, 상하좌우로 이동이 가능하다.
"""

"""
백트래킹
가능한 경우를 탐색하면서 가능하지 않는 경우를 마주쳤을 떄 돌아가는 것
DFS, BFS와 같은 맥락
"""

def check(x):
    """
    x번째 행에 QUEEN을 두어도 괜찮은지 확인
    """
    # 각 이전 행들을 하나씩 확인
    for i in range(x):
        # 위쪽 행에 다른 퀸이 놓여 있으면 False 반환
        if row[x] == row[i]:
            return False
        # 대각선 방향 겹치는게 있다면 False 반환
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    """
    `x`번째 행에 대해 처리 (첫번쨰 행 부터)
    - n번째 행 까지 모두 퀸을 놓을 수 있는 경우엔 `result += 1`
        - 모든 행에 대해 계산

    - x 번째의 행의 각 열(0 ~ N-1)에 퀸을 둔다고 가정한다. 
        - 해당 위치에 Queen을 두어도 괜찮으면 다음 행으로 넘아간다.

    """
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            # 우선, Queen을 두었다고 가정
            row[x] = i
            # 해당 위치에 퀸을 두어도 괜찮은지 `check(x)`
            if check(x):
                dfs(x + 1) # 놓을 수 있다면 다음행으로

n = int(input())
row = [0] * n # 행의 대한 정보
result = 0
dfs(0)
print(result)


