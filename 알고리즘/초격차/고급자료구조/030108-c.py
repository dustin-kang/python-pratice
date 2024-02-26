"""
사이클 게임
중(50분)
https://www.acmicpc.net/problem/20040
"""

n, m = map(int, input().split())

dots = []
for i in range(n):
    dots.append(i)

def find(dots, x):
    if dots[x] != x:
        dots[x] = find(dots, dots[x])
    return dots[x]
    

def union(dots, a, b):

    a = find(dots, a)
    b = find(dots, b)

    if a > b:
        dots[a] = b
    else:
        dots[b] = a

cycle = False # 사이클 발생여부
for _ in range(m):
    a, b = map(int, input().split())

    if find(dots, a) == find(dots, b):
        cycle = True
        print(i + 1)
        break
    else:
        union(dots, a, b)

if not cycle: # 사이클이 발생하지 않는 경우
    print(0)