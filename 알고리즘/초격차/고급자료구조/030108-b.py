"""
연결 요소의 개수
중(40분)
https://www.acmicpc.net/problem/11724

Union-Find 자료구조를 이용해 합치기 연산을 사용하면 된다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

node = []

for i in range(n+1):
    node.append(i)

def find(node, x):
    if node[x] != x:
        node[x] = find(node, node[x])
    return node[x]


def union_find(node, a, b):
    a = find(node, a)
    b = find(node, b)

    if a < b:
        node[b] = a
    else:
        node[a] = b

for _ in range(m):
    a, b = map(int, input().split())

    union_find(node, a, b)

result = set()
for i in range(1, n+1):
    result.add(find(node, i))
print(len(result))