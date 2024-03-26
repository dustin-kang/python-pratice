"""
알파벳
중
https://www.acmicpc.net/problem/1987
"""

R, C = map(int, input().split())

array = [list(map(str, input())) for i in range(R)]

gets = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, array):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if array[nx][ny]