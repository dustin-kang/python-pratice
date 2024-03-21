"""
바이러스
https://www.acmicpc.net/problem/2606
"""
from collections import deque

n, v = int(input()), int(input()) 

array = [[] for _ in range(n+1)]

for i in range(v):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)


visited = [False] * (n+1)

def bfs():
    result = 0
    queue = deque([1])
    while queue:
        v = queue.popleft()
        if not visited[v]:
            result += 1
            visited[v] = True

        for i in array[v]:
            if not visited[i]:
                queue.append(i)
    
    return result

print(bfs()-1)
    


