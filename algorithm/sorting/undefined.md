# 위상 정렬

위상 정렬(Topology sort)는 <mark style="color:orange;">**모든 노드를 방향성을 거스르지 않도록 전체 순서를 계산하는 알고리즘**</mark>입니다. 여기서, 방향성을 거스르지 않는다는 의미는 선 후 관계를 지킨다는 의미입니다. 예를 들어서 아래 그림처럼 딥러닝 과목을 듣기 위해선 데이터 사이언스 과목을 들어야하고 또 머신러닝 과목을 들어야 한다고 합니다. 이렇게 각 노드의 선 후 관계를 지키면서 순서대로 정렬하는 알고리즘을 위상 정렬 알고리즘이라고 합니다.

<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="375"><figcaption></figcaption></figure>

이 알고리즘에서 나오는 개념으로 진입 차수(Indegree)가 있습니다. 진입차수는 특정 노드에 들어오는 간선의 개수를 말합니다. 위 그림, 딥러닝은 진입차수가 2개이고 데이터 사이언스는 0개임을 의미합니다. 그렇다면 진입차수로 위상 정렬 알고리즘을 어떻게 구현할까요?

1. 먼저 진입 차수가 0인 노드를 큐에 넣습니다.
2. 큐가 빌 때 까지 반복합니다.
   1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선들을 제거합니다.
   2. 새롭게 진입차수가 0이 된 노드를 큐에 넣습니다.

<figure><img src="../../.gitbook/assets/Untitled 2.gif" alt=""><figcaption></figcaption></figure>

### 코

```python
from collections import deque

v, e = map(int, input().split())

# 모든 노드에 대한 진입 차수를 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 정보 초기화
graph = [[] for i in range(v + 1)]

# Graph에 간선 정보 입력 받기

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # A -> B
    indegree[b] += 1 # 진입차수 1을 증가

# 위상 정렬 함수
def topology_sort():
    result = [] # 결과를 담을 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0: # 진입 차수가 0일 경우
            q.append(i) # 큐에 해당 노드를 넣습니다.
        
    while q:
        # 큐가 빌때까지 반복
        now = q.popleft()
        result.append(now) # 결과 리스트에 담기

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0: # 진입 차수가 0일 경우
                q.append(i) # 큐에 해당 노드를 넣습니다.



    for i in result:
        print(i, end=' ')

topology_sort()
```

### 시간 복잡도

위상정렬은 수행할 때마다 모든 노드를 확인하면서 해당 노드에서 출발하는 간선들을 제거하므로 **$O(V+E)$**의 시간 복잡도를 갖습니다.
