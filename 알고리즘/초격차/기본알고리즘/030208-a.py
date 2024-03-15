"""
최소 힙
https://www.acmicpc.net/problem/1927
"""
import sys
import heapq
input = sys.stdin.readline

oper = int(input())

# x가 자연수 : 배열에 넣는다.
# x가 0 : 배열에서 빼낸다, (출력한다)


array = [] 

for _ in range(oper):
    x = int(input())
    if x == 0 and array:
        print(heapq.heappop(array))
    elif x == 0:
        print(0)
    else:
        heapq.heappush(array, x)