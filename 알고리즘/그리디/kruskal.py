# Union-Find 서로소 집합 알고리즘 참조
# FIND
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# UNION
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 1. 노드의 개수와 간선 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 2. 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 3. 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 4. 모든 간선 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫번 째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 5. 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하면서
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함시킨다.
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

# 전체 비용 출력
print(result)

print(edges)