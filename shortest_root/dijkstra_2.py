import heapq # 우선순위 큐 사용
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드(N)와 간선(M)의 갯수 입력 받기
n, m = map(int, input().split()) 
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a -(c)-> b
    graph[a].append((b,c))


def dijkstra(start):
    """
    #### 개선된 우선순위 큐
    초기화
    - 시작노드와 거리`(0, start)`를 `q` 우선순위 큐에 삽입 

    반복
    1. 큐에서 최단 거리 노드(`dist`,`now`)를 빼낸다.
    2. 현재 저장된 거리보다 크면 무시
    3. 빼낸 노드의 인접 노드를 `graph`로 확인
         - 저장된 거리보다 작은 경우 갱신하고 우선순위 큐에 삽입
    """
    q = [] # 우선순위 큐
    # 시작노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입한다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않을 때 까지 반복
    while q:
        # 가장 거리가 짧은 노드 빼내기
        dist, now = heapq.heappop(q)
        
        # 만약 해당 노드가 이미 처리된적 있다면 무시
        if distance[now] < dist:
            continue
        
        # 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # 현재 노드 거리 + 연결된 노드의 거리
            if cost < distance[i[0]]: # 다른 노드로 이동하는 거리가 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 노드들 우선순위 큐에 push


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

