"""
DFS와 BFS

https://www.acmicpc.net/problem/1260
"""
from collections import deque

n, m, v = map(int, input().split())
array = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

# 가장 낮은 숫자부터 발견할 수 있도록 정렬!
for i in array:
    i.sort()


# DFS(재귀)
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in array[v]:
        if not(visited[i]):
            dfs(i)

# BFS
def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for i in array[v]:
                if not visited[i]:
                    queue.append(i)


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)