"""
문제집
https://www.acmicpc.net/problem/1766
힙, 위상정렬
"""

# 먼저 푸는게 좋은 문제 : 반드시 먼저 풀어야한다.
# 가능하면 쉬운 문제부터 푼다.
import heapq


n, m = map(int, input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1) # 각 노드마다의 진입차수

# A B : A문제 > B문제로 푸는 게 좋다.
heap = []
result = []

for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b) # 노드에 연결관계를 만든다.
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        # 진입 차수가 0인 경우, 힙에 넣는다.
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]: # 해당 데이터와 연결된 노드 확인
        indegree[y] -= 1 # 간선 제거
        if indegree[y] == 0:
            heapq.heappush(heap,y)

for i in result:
    print(i, end=' ')

