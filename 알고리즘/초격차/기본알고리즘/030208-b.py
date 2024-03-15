"""
카드 정렬하기
https://www.acmicpc.net/problem/1715
"""
import heapq


n = int(input())
array = []
result = 0
for i in range(n):
    heapq.heappush(array, int(input()))

for i in range(n-1):
    one = heapq.heappop(array)
    two = heapq.heappop(array)
    sum_value = one + two
    result += sum_value
    heapq.heappush(array, sum_value)


print(result)
