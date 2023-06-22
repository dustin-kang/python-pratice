# kruskal\_pratice

## \[실전1] 도시 분할 계획

<table data-header-hidden><thead><tr><th width="247.33333333333331"></th><th></th><th></th></tr></thead><tbody><tr><td><a href="../../implementation/implementation.md#메모리-제약-사항">🔗</a></td><td>시간 제한</td><td>메모리 제한</td></tr><tr><td>40분</td><td>2초</td><td>256MB</td></tr></tbody></table>

<figure><img src="../../.gitbook/assets/image (1).png" alt="" width="375"><figcaption></figcaption></figure>

이장님은 위와 같이 N개의 집과 M개의 길로 이루어진 마을에서 마을을 분할할 계획을 세우고 있다.\
&#x20;마을을 분할할 때는 서로 연결되도록 분할해야 한다. 그런데 보니까 마을에는 길이 너무 많다는 생각을 하게 되었다.  두 마을 사이에 길들은 필요가 없으므로 없앨 수 있고 두 집 사이에 경로는 항상 존재하면서도 더 없 수 있다. 그렇다면 나머지 길의 유지비의 합을 최소로 하는 프로그램을 작성하자.

#### 입력 사항

```
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
```

* 첫째 줄에는 집의 갯수 N과 길의 갯수 M이 주어진다. N은 2 이상 100,000 이하의 정수이고 M은 1 이상 1,000,000 이하의 정수이다.
* 그다음 줄부터 M 줄로 걸쳐 길의 정보가 A,B,C 3개의 정수로 공백으로 구분되어 주어진다. _(A집 B집 유지비C)_

#### 출력 사항

```
8
```

* 첫째 줄에 길을 없애고 남은 유지비 합의 최소값을 출력하라.



#### 문제 풀이



### 노드, 간선, 부모 테이블 입력 받

* parent
* edges
* result
* last

```python
# 노드의 개수와 간선 정보 입력받기
v,e = map(int, input().split())
parent = [0] * (v+1)

# 간선을 담을 리스트와 최종 비용
edges = []
result = 0
```

```python
# 부모 테이블에서 우선 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 해 튜플의 첫원소를 cost로 함.
```

```python
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선
```

### 간선을 하나씩 확인하며 사이클 확인하기

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
```

크루스칼 알고리즘에서 최소 신장 트리를 찾은 후 트리를 구성하는 간선 중 가장 비용이 큰 간선(`last`)을 제거합니다.&#x20;

```python
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포
    # 서로의 부모노드가 틀리면 합침 (초기엔 무조건 합침, 자기자신이기 때)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        last = cost # 

print(result - last)
```
