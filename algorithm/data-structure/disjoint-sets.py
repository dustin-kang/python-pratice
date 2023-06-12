"""
해당 알고리즘의 문제점
만약에 노드가 일렬로 연결되어 있다고 가정했을 때, 1 <= 2 <= 3 <= 4 <= 5
노드 5의 루트를 찾기 위해 5부터 1까지 거슬러올라와야 한다. 전체 시간복잡도는 O(VM)이 되어 비효율적이다.
"""

# Find : 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        # 노드 번호와 부모 노드와 일치하지 않는 경우 부모노드 찾을 때 까지 재귀적으로 호출
        return find_parent(parent, parent[x])
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

# 3. union 연산을 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 4. 출력
print('각 원소가 속한 집합 : ', end= " ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end= " ")
for i in range(1, v + 1):
    print(parent[i], end=' ')