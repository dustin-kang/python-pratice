"""
도서관
https://www.acmicpc.net/problem/1461
"""
import heapq

n, m = map(int, input().split(" ")) # 책의 개수, 옮길수 있는 책의 개수(M)
array =  list(map(int, input().split()))
largest = max(max(array), -min(array)) # 39 가장 거리가 먼 거리

minus = []
plus = []

for i in array:
    if i > 0:
        heapq.heappush(plus, -i) # 최대 힙!
    else:
        heapq.heappush(minus, i)
# 각 책들을 제자리에 둘 수 있는 최소 걸음의 수

result = 0

while plus:
    result += heapq.heappop(plus) # 한번에 매번 M개씩 옮긴다고 가정
    for _ in range(m-1):
        if plus:
            heapq.heappop(plus)

while minus:
    result += heapq.heappop(minus) # 한번에 매번 M개씩 옮긴다고 가정
    for _ in range(m - 1):
        if minus:
            heapq.heappop(minus)

print(-result * 2 - largest) # 욍복 거리 중 편도 거리를 제외
# (39 + 29 + 6 +  11) * 2 - 39 = 131