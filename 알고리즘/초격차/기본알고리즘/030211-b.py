"""
숨바꼭질

https://www.acmicpc.net/problem/1697
"""
from collections import deque
n, k = map(int, input().split()) # 수빈이 점, 동생 점

# 걷거나 순간이동으로 동생을 빠른 시간내 찾는다.

# 걷기 : 1초 후 X+1, X-1
# 순간이동 : 1초 후 2*X

MAX = 100_001
queue = deque([n])
count = 0
visited = [0] * MAX # 이전 방문 + 1

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        
        for next in (v - 1, v + 1, v * 2): # 걷기, 순간이동 중 방문 이력이 있는 지 확인
            if 0 <= next < MAX and not visited[next]:
                visited[next] = visited[v] + 1
                queue.append(next)

print(bfs(n))   

