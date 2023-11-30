"""
그래프 - 도시 분할 계획

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
"""
# 길이 많아 최소 비용의 경로를 구하자. 최소 신장 트리 -> 크루스칼 알고리즘 -> Union-Find

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1) # 0. 부모테이블 생성

edges = []
result = 0 # 최종 비용

# 0. 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i 

for _ in range(e):
    a, b, cost = map(int, input().split()) # 간선 정보 받기
    edges.append((cost, a, b)) # 비용, A, B

# 비용 순으로 정렬
edges.sort() # [(1, 3, 2), (1, 6, 4), (2, 1, 3), (2, 1, 6), (2, 2, 5), (3, 1, 2), (3, 4, 5), (3, 6, 5), (4, 3, 4), (4, 6, 7), (5, 5, 1), (6, 7, 3)]
last = 0


# Union-Find #
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 합치기
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost # 최소 신장 트리를 만드는 데 필요한 전체 비용
        last = cost # 가장 비용이 큰 간선

print(result - last) # 가장 비용이 큰 간선 제거


