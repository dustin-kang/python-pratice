"""
효율적인 해킹
https://www.acmicpc.net/problem/1325
"""
from collections import deque

N, M = map(int, input().split())
array = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    array[b].append(a) # B를 해킹하면 A도 해킹할 수 있다.

result = []
max_value = -1

def bfs(v):
    # 정점의 갯수가 방문하는 수(count)를 계산
    queue = deque([v])
    visited = [False] * (N + 1)
    visited[v] = True

    count = 1
    while queue:
        v = queue.popleft()
        for e in array[v]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                count += 1
    
    return count

for i in range(1, N+1):
    C = bfs(i)

    # count가 가장 큰 정점이 담길 수 있도록 계산, 만약 동일하면 추가 
    if C > max_value:
        result = [i]
        max_value = C
    elif C == max_value:
        result.append(i)
        max_value = C

for e in result:
    print(e, end=' ')
