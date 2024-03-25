"""
컵라면
https://www.acmicpc.net/problem/1781
"""

import sys, heapq

input = sys.stdin.readline

n = int(input()) # 숙제
array = []
queue = []

for i in range(n):
    d, c = map(int,input().split())
    array.append((i+1, d, c))

array.sort(key=lambda x: (x[1])) # 데드라인이 낮은 수 순서로 정렬

for i in array:
    dead = i[1] 
    heapq.heappush(queue, i[2])
    if dead < len(queue): # 데드라인을 초과하면 문제를 풀 수 없다.
        heapq.heappop(queue)

print(sum(queue))