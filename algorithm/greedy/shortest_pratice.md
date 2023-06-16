# shortest\_pratice

> **INDEX**
>
> * [실전 문제](shortest\_pratice.md#실전1-1로-만들기) : 미래도시
> * 실전문제 : 전보

## \[실전1] 미래도시

<table data-header-hidden><thead><tr><th width="247.33333333333331"></th><th></th><th></th></tr></thead><tbody><tr><td><a href="../../implementation/implementation.md#메모리-제약-사항">🔗</a></td><td>시간 제한</td><td>메모리 제한</td></tr><tr><td>40분</td><td>1초</td><td>128MB</td></tr></tbody></table>

공중 미래도시에는 1번부터 N번 까지 회사가 있는데 서로 도로를 통해 연결이 되어있다. **방문 판매원 A는 현재 1번 회사에 위치해 있으며 X번 회사에 방문해 물건을 판매하고자 한다.** 공중 미래도시는 특정 회사에 도착하기 위한 방법으로 회사끼리 연결되어 있는 도로를 이용해 가는 방법이 유일하다. 또한 연결된 2개의 회사는 양방향으로 이동이 가능하다. (1만큼의 시간으로 이동이 가능하다.)

또, 방문 판매원 A씨가 K번 회사에 존재하는 소개팅 상대도 만나야 하기 때문에 1번 회사 -> K번 회사 -> X번 회사로 가야 한다. 이때 A씨는 최대한 빠르게 이동하고자 한다. 이때 방문 판매원이 회사 사이를 이동하는 최소 시간을 프로그램으로 작성하시오.&#x20;

예를 들어, N = 5, X =4, K = 5일 때, 회사간 도로가 7개라면, 아래와 같이 도로가 가정할 수 있다.

```
(1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)
```

이때, 방문 판매원 A씨는 (1->3->5->4) 순으로 가야 하기 때문에 총 3만큼의 시간으로 이동할 수 있다.&#x20;

#### 입력 사항

```
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
```

```
4 2
1 3
2 4
3 4
```

* 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다. (1≤N,M ≤ 100)
* 둘째 줄부터 M + 1번째 줄에는 두회사의 번호가 공백으로 이루어진다.
* ﻿﻿M + 2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 ≤ K ≤ 100)

#### 출력 사항

```
3
```

```
4
```

* &#x20;첫째 줄에 방문 판매원 시가 시번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
* 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

#### 문제 풀이

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

전형적인 플로이드 워셜 알고리즘 문제로 <mark style="color:green;">**N의 범위가 100 이하라서 빠르게 풀 수 있는 문제**</mark>입니다. &#x20;

```python
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 양방향 그래프이고 서로 가는 비용이 1임.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 1 -> X -> K
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], (graph[a][k] + graph[k][b]))

# 수행된 결과 출력 1 -> k -> x
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
```

## \[실전2] 전보

<table data-header-hidden><thead><tr><th width="247.33333333333331"></th><th></th><th></th></tr></thead><tbody><tr><td><a href="../../implementation/implementation.md#메모리-제약-사항">🔗</a></td><td>시간 제한</td><td>메모리 제한</td></tr><tr><td>60분</td><td>1초</td><td>128MB</td></tr></tbody></table>

각 도시는 다른 도시로 메시지를 전송할 수 있다. 그러나, 만약에 X라는 도시에서 Y라는 도시로 메세지를 보내려면 X와 Y간의 통로가 설치되어 있어야 한다. X->Y 통로는 있으나 X<-Y 통로가 없는 경우에는 Y에서 X로 메시지를 보낼 수 없다. 또한, 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

어느날, C라는 도시가 위급상황이 발생해 최대한 많은 도시에 메시지를 보내려고 한다면, 도시 C에서 보낸 메시지를 받게되는 도시는 총 몇 개이며 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

#### 제한 사항

* 첫째 줄에는 도시의 개수 `N` 과 통로의 갯수 `M` , 메시지를 보내고자 하는 도시 `C` 가 주어집니다.
  * (1 ≤ `N` ≤ 30,000, 1 ≤ `M` ≤ 200,000, 1 ≤ `C` ≤ `N`)
* 둘째 줄 부터는 M+1 번째 줄에 걸쳐 통로에 대한 정보 `X,Y,Z` 가 주어집니다. X도시에서 Y 도시까지 가는데 Z시간이 걸리는 것을 의미합니다.
  * (1 ≤ `X`, `Y` ≤ `N,` 1 ≤  `Z` ≤ 1,000)
* 출력은 도시C에서 보낸 메시지를 받은 도시의 개수와 걸리는 시간을 공백으로 구분하여 출력합니다.

```
3 2 1
1 2 4
1 3 2
```

```
2 4
```

#### 문제 풀이

한 도시에서 다른 도시까지의 최단 거리를 구하는 문제이므로 다익스트라 알고리즘을 이용해 풀 수 있다.&#x20;

그리고 N과 M의 범위가 크기 때문에 우선순위 큐를 이용해 작성해야한다.&#x20;

```python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split()) # 도시, 간선, 시작노드
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z)) # x도시가 y도시 가는 통로 Z시간


# 다익스트라 알고리즘
def dijkstra(start):
    q = [] # 우선순위 큐
    # 시작 도시의 최단 경로를 담습니다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 최단 경로보다 크다면 
            continue # 무시
        
        for i in graph[now]: # 인접노드를 꺼내기
            cost = dist + i[1] 
            if cost < distance[i[0]]: # 인접 노드의 거리보다 작을 경우
                distance[i[0]] = cost # 갱신
                heapq.heappush(q, (cost, i[0])) # 노드들 우선순위 큐에 push

dijkstra(start)

count = 0 # 도시의 갯수
max_distance = 0 # 도시들이 메세지를 받는데 걸리는 시간

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
# 시작 노드를 제외하므로 count - 1
print(count - 1, max_distance)
```

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
