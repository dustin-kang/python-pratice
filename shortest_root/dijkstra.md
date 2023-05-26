# Dijkstra(다익스트라,데이크스트라) 알고리즘

> 방문하지 않은 노드 중에서 **가장 거리가 짧은(최단 경로)인 노드를 선택**하면서 모든 원소를 순차 탐색하는 알고리즘

- 다익스트라 알고리즘은 반드시 음의 간선이 없을 때 정상적으로 동작합니다. (음의 간선이란, 0 미만의 `-`수를 가지는 간선을 의미합니다.)

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화 ( = 각 노드에 대한 최단 거리정보가 있음)
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 (현재 기준에서 가장 짧은 노드를 확인)
4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산해서 테이블 갱신

3,4 번 반복

Dijkstra 알고리즘은 두 가지의 구현 방법으로 나뉠 수 있습니다.
- 구현 방법1 ) 구현은 쉬우나 느리게 동작하는 코드
- 구현 방법 2 ) 구현은 어려우나 빠르게 동작하는 코드


## 간단한 다익스트라 알고리즘
> **노드가 5,000개 이하의 경우** 사용이 가능한 알고리즘입니다.


![Untitled](https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/f0c1cef7-180e-4e93-8ed8-22efede7fa5f)

- 시간복잡도 : $O(V^2)$
- [코드 파일 바로가기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/shortest_root/dijkstra_1.py)

## 개선된 다익스트라 알고리즘
> **노드의 개수가 10,000개를 넘어가는 문제**일 때 사용이 가능한 알고리즘입니다.

- 시간복잡도 : $O(ElogV)$
- 개선된 알고리즘에서는 [힙(Heap)]()구조를 사용합니다.
  - 특정 노드까지의 거리를 힙에 담아 더욱 빠르게 처리할 수 있어 로그 시간이 걸립니다.
- [코드 파일 바로가기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/shortest_root/dijkstra_2.py)

```py
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
```