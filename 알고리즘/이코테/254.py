"""
DFS/BFS - 미로탈출

5 6
101010
111111
000001
111111
111111

-> 10

3 3
110
010
011

-> 5
"""

from collections import deque

n, m = map(int, input().split())
dirs = [(-1,0),(0,1), (1,0),(0,-1)]

maps = [list(map(int, input())) for i in range(n)]

def bfs(x=0, y=0):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = dirs[i]
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 # 방문한 위치는 +1씩 추가 
                queue.append((nx, ny))
    return maps[n-1][m-1]

print(bfs())

