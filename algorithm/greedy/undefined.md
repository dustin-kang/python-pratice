# 서로소 집합

#### 서로소 집합 (Disjoint Sets)

공통원소가 없는 두 집합을 의미합니다. 에를들어, `{1, 2}` 와 `{3, 4}` 는 공통 원소가 존재하지 않기 때문에 서로소 관계이고 `{1, 2}` 와 `{2, 3}` 은 공통 원소가 존재하므로 서로소 관계 인 것입니다.

## 서로소 집합 자료구

서로소 집합 자료구조는 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조입니다. 서로소 집합 자료구조는 2가지의 연산으로 이루어져 있습니다.

* Union (합집합)
* Find (찾기)&#x20;

서로소 집합 자료구조는 **트리 구조를 이용해 집합을 표현**하는데 이는 다음과 같습니다.

만약 아래의 원소들이 있고, 집합 연산도 아래와 같을 때 입니다.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

여기서 `union 2, 4` 는 현 루트 노드가 각각 4 -> 1, 2 -> 2 이기 때문에 2의 부모를 1로 설정합니다.

이 알고리즘에서 가장 유의할 점은 반드시 부모 테이블(`parent`)을 항상 가지고 있어야한다는 것입니다. 부모 테이블을 통해 루트노드로 거슬러 올라가야 하기 때문입니다.&#x20;

```python
"""
이전 문제점에서 개선된 점
- 비효율적인 시간복잡도를 줄이기 위해 경로 압축 기법을 사용했다.
- 사이클 여부에 따라 종료할 건지 합집합을 수행할 건지 나눔

V + Mlog2V의 시간 복잡도가 발생한다. 물론 줄이는 방법은 다양하다.
"""

# Find : 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        # 노드 번호와 부모 노드와 일치하지 않는 경우 부모노드 찾을 때 까지 재귀적으로 호출
        parent[x] = find_parent(parent, parent[x]) # 경로 압축 기법
    return x # 그게 아니면 자신 노드 호출

# Union : 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 부모노드 갱신
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

# 1. 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화 

# 2. 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# # 3. union 연산을 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

cycle = False

# 3,5. 사이클 판별하기
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        # 루트 노드가 서로 같은 경우, Cycle이 발생한 것이다.
        cycle = True
        break
    else:
        # 루트 노드가 서로 다른 경우, union을 실행한다.
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

# 4. 출력
print('각 원소가 속한 집합 : ', end= " ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end= " ")
for i in range(1, v + 1):
    print(parent[i], end=' ')

```

### &#x20; 시간 복잡도

<mark style="color:purple;">**경로 압축 방법**</mark>을 적용한 시간 복잡도는 약 O(V + Mlog2V)의 복잡도를 가지고 있습니다. 물론 이 방법 말고도 다른 방법이 존재하긴합니다.

### 사이클 판별

서로소 알고리즘은 무방향 그래프 내에서 사이클을 판별할 수 있다는 특징을 지녔습니다.  간선을 하나씩 확인해가면서 두 노드가 포함되어 있는 집합을 합치는(union) 과정을 반복하면서 사이클을 판별할 수 있니다. 이 알고리즘은 간선에 방향성이 없을 때 가능합니다.

> 방향이 있는 그래프에 경우, DFS 알고리즘을 이용하여 판별할 수 있습니다.

