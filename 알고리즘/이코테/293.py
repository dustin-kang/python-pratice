"""
최단 경로 - 전보

3 2 1
1 2 4
1 3 2

2 4
"""

import heapq
import sys

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
INF = int(1e9) # 무한대에서 점점 줄여갈 최단 경로
distance = [INF] * (n+1) 

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) # x 노드에서 y노드로 가는 비용이 z

"""
graph = [][(2, 4), (3, 2)][][]
distance = [ 무, 무, 무, 무 ]
"""

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 현재까지 최단 경로, 도착 지점
    distance[start] = 0 # 지점의 거리

    """
    distance = [무, 0, 무, 무]
    q = [(0,1)]
    """

    while q:
        dist, now = heapq.heappop(q) # 0, 1
        if distance[now] < dist:  
            continue

        for i in graph[now]:
            cost = dist + i[1] # dist + z
            # 현재 노드를 거쳐 다른 노드로 이동하는 게 기존 거리보다 더 짧은 경우, 기존 거리에 업데이트
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # cost, y

"""
1. 
distance = [무, 0, 4, 2]
cost = 0 + 4, 0 + 2 # 현재 비용 + 다음 노드로 가기 위한 비용
q = [(4, 2), (2, 3)]

2.
distance = [무, 0, 4, 2]
q = [(4, 2)]

3. 
distance = [무, 0, 4, 2]
q = []
"""


dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count +=1
        max_distance = max(max_distance, d)

print(count-1,  max_distance)


