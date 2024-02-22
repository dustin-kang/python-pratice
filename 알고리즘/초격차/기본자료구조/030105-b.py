"""
트럭
40분(중)
https://www.acmicpc.net/problem/13335

- 다리가 가득 찼으면 다리에서 원소를 추출한다.(한칸씩이동)
- 트럭 배열에서 하나씩 큐에 삽입 한다.
- 만약 트럭을 다리에 넣을 수 없다면 0을 삽입한다.

"""

from collections import deque

time = 0
n,w,L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([])

time = 0
while sum(trucks) > 0:
    if sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft()) 
        time += 1
    else:
        bridge.append(0)

    if len(bridge) == w:
        bridge.popleft()
        time += 1



print(time - len(bridge))


