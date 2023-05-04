> #### 사전 개념
> - [stack, queue](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/data-structure/stack_queue.md)
> - [recursive_func](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/data-structure/recursive_function.md)

설명하기 앞서, BFS와 DFS는 그래프의 기본 구조로 이루어져 있다.
그래프는 **Node**와 **Edge**로 이루어져 있으며 두 Node가 하나의 Edge로 연결되있다면 `두 노드는 인접하다(Adjacent)`라고 할 수 있다.

여기서 그래프는 크게 두가지 방식으로 표현할 수 있는데 인접 행렬과 인접 그래프로 설명할 수 있다.
- **인접 행렬(Adjacency Matrix)** : 2차원 배열로 그래프의 연결 관계를 표현
- **인접 그래프(Adgacency Graph)** : 리스트로 그래프의 연결 관계를 표현


||인접 행렬|인접 그래프|
|---|---|---|
|특징|2차원 배열에 노드의 연결 형태를 기록|모든 노드에 연결된 노드에 대한 정보를 차례대로 기록|
|메모리 측면|모든 관계를 저장하므로 노드 갯수가 많을 수록 낭비 👎|연결된 정보만 저장하므로 효율적 👍|
|속도 측면|인덱스를 통해 바로 찾을 수 있어 👍|연결 정보만 얻기 때문에 느림 👎|

```python
# 인접 행렬
INF =  99999999 # 연결이 되지 않은 노드 표현

graph = [
  [0, 7, 5], 
  [7, 0, INF],
  [5, INF, 0],
]

print(graph)

# [[0, 7, 5], [7, 0, 99999999], [5, 99999999, 0]]

# 인접 리스트
# 행이 3개인 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((0, 5)) # 노드, 엣지

print(graph)

# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]

```

# DFS (Depth First Search)
> 특정 경로를 탐색하다가 특정 상황에 깊이 들어가 노드들을 방문하고 다시 돌아오는 알고리즘을 말합니다. **최대한 멀리 있는 노드부터 우선적**으로 탐색합니다.

#### 1. 탐색 노드를 스택에 삽입하고 방문 처리 한다.
#### 2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있는 경우 인접노드를 스택에 넣고 방문한다. (방문하지 않은 인접 노드가 없다면 최상단 노드를 꺼낸다.)

- 인접 노드 중 방문하지 않는 노드들이 여러개 일 경우 번호가 낮은 순서대로 방문합니다.

![DFS1](https://user-images.githubusercontent.com/55238671/236117539-3b1048f6-ed88-4b23-989a-515323f49533.gif)

깊이 우선 탐색 알고리즘은 스택 자료구조에 기초를 두고 있어 구현이 간단합니다. 하지만 실제로 스택(Stack)을 굳이 사용하지 않아도 되며 재귀 함수를 이용하면 간결하게 구현할 수 있습니다.

시간 복잡도는 데이터 갯수를 한번씩 돌며 수행하기 때문에 **$O(N)$** 입니다.

### 코드
```py
def dfs(graph, v, visited):
  """
  param:
  - graph : 그래프
  - v : 탐색 시작 노드
  - visited : 방문 체크 용 리스트
  """
  visited[v] = True
  print(v, end=' ')

  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]: # 방문하지 않은 노드라면
      dfs(graph, i, visited)

# 각 노드가 연결된 정보를 인접리스트로 표현 (2차원)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 방문된 정보를 체크하는 리스트 자료형
visited = [False] * 9

dfs(graph, 1, visited)
```

재귀함수 대신 스택을 이용하면 **스택에 들어간 순서대로 출력**이 됩니다. [참고자료]()


# BFS (Breadth First Search)
> 최대한 가까운 노드부터 탐색하는 알고리즘입니다.

#### 1. 탐색 노드를 큐에 삽입하고 방문 처리 한다.
#### 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않는 노드를 모두 큐에 삽입하고 방문 처리 한다.

![BFS](https://user-images.githubusercontent.com/55238671/236124749-4d82f713-3eaf-4359-947e-ae6819cf7b1a.gif)


너비 우선 탐색 알고리즘은 큐 자료구조를 기반으로 두고 있습니다. 실제로 `deque` 라이브러리를 사용하면 좀더 편하게 구현할 수 있습니다. 

시간복잡도는 마찬가지로 N 개의 데이터를 모두 방문하므로 $O(N)$의 시간복잡도입니다.

> 실제로 수행시간은 DFS보다 빠른 편입니다. 

### 코드
```python
from collections import deque

def bfs(graph, start, visited):
  """
  params:
  - graph : 그래프
  - start : 탐색 시작 노드
  - visited : 방문 체크 용 리스트
  """
  # Deque 라이브러리를 이용해 Queue 구현
  
  queue = deque([start])
  visited[start] = True # 현재 노드 방문 처리

  # 큐가 빌때 까지 반복
  while queue:
      v = queue.popleft()
      print(v, end = '')

      # 큐에서 노드를 꺼내면 해당 노드와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v]:
        if not visited:
          queue.append(i)
          visited[i] = True


# 각 노드가 연결된 정보를 인접리스트로 표현 (2차원)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 방문된 정보를 체크하는 리스트 자료형
visited = [False] * 9

bfs(graph, 1, visited)
```

## 정리

||DFS|BFS|
|---|---|---|
|동작 원리|스택|큐|
|구현 방법|재귀 함수|큐 자료구조, deque|
|과정1|스택에서 노드를 꺼내 방문하지 않은 인접 노드를 스택에 넣고 방문 처리|큐에서 노드를 꺼내 방문하지 않은 인접 노드 모두 큐에 넣고 방문처리|
|과정2|방문 가능한 노드가 없으면 스택에서 최상단 노드 꺼냄|방문 가능한 노드가 없으면 무시|

> 코딩테스트에서 **2차원 배열의 탐색 문제**가 있다면 그래프 형태로 바꾸서 풀이하면 된다.

---
- [실전문제 : 음료수 얼려먹기]()
- [실전문제 : 미로탈출]()
