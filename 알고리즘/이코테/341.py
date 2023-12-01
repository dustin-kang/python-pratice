"""
그래프 - 여행 계획
여행 가능 여부 판단하는 문제로 여행 계획 순서에 있는 여행지가 같은 집합에 있어야 함 -> 서로소 집합

여행지, 여행 계획에 속한 도시수
연결되어 있는 지  여부(n)
여행 계획 순서

5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0 
1 0 0 0 0
2 3 4 3

YES
"""

n, m = map(int, input().split())
parent = [0] * (n+1)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[a] = b
    else :
        parent[b] = a


for i in range(n):
    parent[i] = i


# UNION 연산 수행 #
for i in range(n):
    data = list(map(int, input().split())) # 여행지 하나씩 가져오기
    for j in range(n):
        if data[j] == 1: # 연결된 여행지라면 
            union(parent, i+1, j+1) # 합치기 


routes = list(map(int, input().split())) # 여행 순서

# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인 #
result=True
for i in range(m-1): # 0 1 2
    if find(parent, routes[i]) != find(parent, routes[i+1]): # 0 ==? 1 , 1 ==? 2 ...
        result = False

if result:
    print("YES")
else:
    print("NO")

