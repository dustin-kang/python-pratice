"""
dfs/bfs = 경쟁적 전염

1초마다 상하좌우로 바이러스 증식
S초가 지난 후 바이러스가 존재하지 않으면 0 출력
X,Y 축에 있는 바이러스 출력

>> 각 바이러스는 낮은 번호 순으로 증식한다.

3 3 => n X M
1 0 2
0 0 0
3 0 0
2 3 2 => s, x, y
"""
from collections import deque

n,m = map(int, input().split())

graph = [] # 전체 보드
data = [] # 바이러스 정보
# 그래프에 대입을 하면서 바이러스 정보 리스트 만들기!
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 좌표


data.sort()
q = deque(data) # 초마다 번지게 할 예정

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    virus, s, x, y = q.popleft()
    # 해당 시간이 되면 종료
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])


    



