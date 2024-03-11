"""
좌표 정렬하기
15분
"""

n = int(input())
array = []

for i in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort(key= lambda x: (x[0], x[1]))

for i in array:
    print(i[0], i[1])