"""
유기농 배추
DFS
https://www.acmicpc.net/problem/1012
"""
import sys
sys.setrecursionlimit(1000000)


ts = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    # 방문하면서 True 처리 해버리기
    check[x][y] = True
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        # 이차원 배열에 포함되어 있는 경우에만 dfs!
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if array[nx][ny] and not check[nx][ny]:
            dfs(nx, ny)


for _ in range(ts):
    r, c, l = map(int, input().split())
    array = [[0] * c for _ in range(r)]
    check = [[False] * c for _ in range(r)]

    for _ in range(l):
        x, y = map(int, input().split())
        array[x][y] = 1

    result = 0

    for i in range(r):
        for j in range(c):
            if array[i][j] and not check[i][j]:
                dfs(i,j)
                result += 1    

    print(result)
    
