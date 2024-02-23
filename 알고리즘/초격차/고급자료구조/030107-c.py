"""
소수의 곱
중상(60분)
https://www.acmicpc.net/problem/2014
"""
import sys, heapq
input =  sys.stdin.readline

k, n = map(int, input().split())
array = list(map(int, input().split()))

heap = []
visited = set() # 이미 처리된 수 기록
max_value = max(array) # 최대값

for x in array:
    heapq.heappush(heap, x)

for i in range(n-1): # n-1 번째 까지 heap에서 빼내기
    element = heapq.heappop(heap) # 힙에서 원소 하나를 꺼낸다.
    
    for x in array:
        now = element * x # 곱한 결과를 계산한다.

        if len(heap) >= n and max_value < now:
            continue
        if now not in visited: # 처음 방문하는 수일 경우
            heapq.heappush(heap, now) # 힙에 넣기
            max_value = max(max_value, now)
            visited.add(now) # 방문 여부 기록

print(heapq.heappop(heap))


# 힙의 크기가 N 이상이고 힙의 최댓값보다 곱한 결과가 크다면 넣을 필요 없다
# 한번 구한 결과는 다시 넣을 필요는 없다.

