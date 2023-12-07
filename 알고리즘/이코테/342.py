"""
그래프 - 탑승구
G개 탑승구와 P개의 비행기가 도착한다.
한개의 비행기는 무조건 한개의 탑승구와 도킹해야한다.
그러나 순서대로 도킹하다 어떤 탑승구에도 도킹할 수 없는 비행기가 나오는 경우 중지된다.
최대한 많은 비행기를 도킹하고자할 때 얼마나 많이 도킹할 수 있을까?

4 탑승구 수
3 비행기 수
4 각 비행기가 도킹할 수 있는 탑승구 정보
1
1
"""

g = int(input())
p = int(input())
parent = [0 for i in range(g+1)]

for i in range(1, g+1):
    parent[i] = i # [0, 1, 2, 3, 4]

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

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기(p)와 탑승구 루트 확인(parent)
    if data == 0: # 현재 루트가 0이라면 종료
        break
    union_parent(parent, data, data-1) # 그렇지 않으면 왼쪽 집합과 합치기
    result += 1

# 4, 3 result = 1
# 1, 0 result = 2
# 1, 0
print(result)