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
