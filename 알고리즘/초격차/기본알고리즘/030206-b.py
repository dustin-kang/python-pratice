"""
중량제한
https://www.acmicpc.net/problem/1939

3 3
1 2 2
3 1 3
2 3 2
1 3
"""
from collections import deque

start = 10000000
end = 1
n, m = map(int, input().split())
array = [[] for _ in range(m+1)]

for i in range(m):
    a, b, kg = map(int, input().split())
    array[a].append((b, kg))
    array[b].append((a, kg))
    start = min(start, kg) # 최소 중량 초기값 2
    end = max(end, kg) # 최대 중량 초기값 3

A, B = map(int, input().split())

def bfs(c):
    """
    경로 있는지 탐색하는 알고리즘
    """
    queue = deque([A])
    visited = [False] * (n+1)
    visited[A] = True # 출발 노드 True

    while queue:
        x = queue.popleft() 
        for y, kg in array[x]:
            if not visited[y] and kg >= c: # 현재 중량보다 무거운 경우 방문 처리
                visited[y] = True # 방문 처리
                queue.append(y)
    return visited[B]

result = start
while(start <= end): # 최대 중량 제한을 넘으면 종료
    mid = (start + end) // 2 # 현재 중량
    if bfs(mid): # 이동이 가능한 경우 중량을 증가
        result = mid
        start = mid + 1
    else: # 이동이 불가능한 경우 중량을 감소
        end = mid - 1

print(result)
