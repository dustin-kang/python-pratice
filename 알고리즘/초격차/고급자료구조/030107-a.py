"""
절댓값 힙
40분(중)
https://www.acmicpc.net/problem/11286
"""

import heapq # 우선순위 큐
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    value = int(input())
    if value == 0:
        # 삭제 연산 : 절댓값이 가장 작은 값을 출력
        if len(heap) == 0:
            # 0 출력 : 힙이 비어있는 경우
            print(0) 
        else:
            abssolute, original = heapq.heappop(heap)
            print(original)
    else:
        # 삽입 연산 : 값을 넣는다.
        heapq.heappush(heap, (abs(value), value))