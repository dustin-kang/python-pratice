"""
배

https://www.acmicpc.net/problem/1092
"""

import sys

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0

## 모든 박스를 옮길 수 없는 경우
if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

## 각 크레인 별 현재 옮겨야 하는 박스의 번호
positions = [0] * n
## 각 박스를 옮겼는지 여부
checked = [False] * m

while True:
    if count == len(boxes): # 박수를 다 옮겼으면 종료
        break
    for i in range(n):
        while positions[i] < len(boxes):
            # 아직 옮긴 박스 중 옮길 수 있는 박스를 만날때 까지 반복
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result +=1
print(result)

