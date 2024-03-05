"""
성지키기

https://www.acmicpc.net/problem/1236
"""

n , m = map(int, input().split()) # 세로, 가로

# 행, 열 기준으로 경비병이 필요하다. 어느 행, 열이라도 비어있으면 안된다.

array = []
for _ in range(n):
    array.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1


row_count = 0
col_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

for j in range(m):
    if column[j] == 0:
        col_count += 1

print(max(row_count, col_count))