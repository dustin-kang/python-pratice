"""
그래프 - 팀 결성 (union-find)

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1 
"""



def union(parent, a, b):
    # 2-a. 팀 합치기
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(parent, x):
    # 2-b. 같은 팀 여부 확인
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


n, m = map(int, input().split()) # 사람 수, 연산 수
parent = [0] * (n+1)

# 1. 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i


# 2. 연산 시작
for i in range(m):
    oper, a, b = map(int, input().split()) # 연산, a, b
    if oper == 0:
        # 팀합치기
        union(parent, a, b)
    else:
        # 같은 팀 여부 확인
        if find(parent, a) == find(parent, b):
            print(True)
        else:
            print(False)