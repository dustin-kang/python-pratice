"""
DFS/BFS - 감시 피하기

3개의 장애물 개수가 주어졌을 때, 장애물 뒷편에 숨은 학생은 선생님이 볼 수 없다.
그렇다면 장애물 개수(3개)에 따른 장애물을 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 YES,NO로 나타내라.
N(3<=N<=6)은 N개의 줄을 의미한다.

5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

YES

4
S S S T
X X X X
X X X X
T T T X

NO


"""
from itertools import combinations

# 먼저 단순하게 2차원 배열만 만들지 않고 선생님의 감시를 위해 선생님 배열과 빈 공간 배열을 담는다..
n = int(input())
board = []
teachers = [] # 선생님
spaces = [] # 빈공간

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direct):
    """
    ### 특정 방향에 따라 감시 진행
    - `True` : 학생을 발견한 경우
    - `False`: 학생을 발견하지 못한 경우

    `direct` 마다 최대 혹은 최소 위치까지 검사,
    만약 장애물(`O`)을 발견하거나 아무 것도 없으면 `False`
    학생(`S`)를 발견하면 `True`
    """
    if direct == 0:
        # 👈
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if direct == 1:
        # 👉
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    if direct == 2:
        # 👆
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if direct == 3:
        # 👇
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False  # 아무것도 없는 경우

def process():
    """
    장애물을 설치한 다음,
    ### 한명이라도 학생이 감지되는지 검사
    """
    for x,y in teachers:
        for direct in range(4): # 상하좌우
            if watch(x,y, direct):
                return True
    return False

find = False

# 빈공간에서 3개의 장애물을 돌아가면서 모든 조합을 확인한다.
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    # 장애물을 설치했는데 한명도 감지가 안되는 경우
    if not process():
        find = True
        break
    # 다시 다른 조합을 위해 장애물을 제거
    for x,y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")