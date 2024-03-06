"""
공유기 설치
https://www.acmicpc.net/problem/2110

log (X) * N

5 3
1
2
8
4
9
"""

n, c = map(int, input().split()) # 집, 공유기
array = []
for i in range(n):
    array.append(int(input()))

array  = sorted(array)

near = array[1] - array[0] # 가장 가까운 거리
far = array[-1] - array[0] # 가장 먼 거리
result = 0

while(near <= far):
    """
    최소 gap과 최대 gap이 같아질 때까지 반복하면서
    near 증가
    """
    mid = (near + far) // 2
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우
        near = mid + 1
        result = mid
    else: # C개 이상의 공유기를 설치할 수 없는 경우
        far = mid - 1

print(result)





