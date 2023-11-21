"""
BFS/DFS - 음료수 얼려먹기

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""

n, m = map(int, input().split())
"""
💡
만약 해당 좌표가 0이면 1로 바꾸고 result += 1 하는 시스템
추가로 주변 좌표가 중복하지 않게 DFS로 확인
"""

# 2차원 그래프 만들기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 범위에 벗어나면 False
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False # 1이면 False

# 근본 코드 
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)