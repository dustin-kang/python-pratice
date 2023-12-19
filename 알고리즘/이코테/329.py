"""
이진탐색 - 공유기 설치

5 3
1
2
8
4
9
"""

n, c = map(int, input().split())
homes = [int(input()) for i in range(n)]
homes.sort()

result = 0
start = 1 # 1 : 가능한 최소 거리
end = homes[-1] - homes[0] # 8 : 가능한 최대 거리

while(start<= end):
    mid = (start + end) // 2 # 4 : start 공유기와 end 공유기 사이의 거리
    value = homes[0] # 공유기 설치 위치
    count = 1
    for i in range(1, n): # 공유기 설치 
        if homes[i] >= value + mid: # 제한된 공유기 거리를 넘게되면 value에 새로 공유기 설치
            value = homes[i]
            count += 1
    if count >= c: 
        start = mid + 1
        result = mid
    else: # 공유기를 다 설치하지 못한 경우 거리 감소해서 나머지 공유기를 설치
        end = mid - 1

print(result)