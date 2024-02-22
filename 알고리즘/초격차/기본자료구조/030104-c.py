"""
회전하는 큐
회전 연산의 최소값 출력
30분
https://www.acmicpc.net/problem/1021
"""
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
array = deque([i for i in range(1, n+1)])
targets = list(map(int, input().split())) # 뽑아낼 원소 목록
cnt = 0 # 회전 연산 수


for target in targets:
    target_index = array.index(target)
    """
    # 왼쪽으로 갈까 오른쪽으로 갈까 (중간 점과 비교)
    - 왼쪽이 더 빠른 경우 : 중간지점보다 작은 위치의 경우, 앞 데이터를 빼 뒤로 넘긴다.
    - 오른쪽이 더 빠른 경우 : 중간지점보다 큰 위치의 경우, 뒤 데이터를 뺴 앞으로 넘긴다.
    # 짝수 홀수
    - 짝수의 경우 왼쪽이 가까울 때 : [OOO|OXX]
    - 홀수의 경우 왼쪽이 가까울 때 : [OOO|XX]
    """
    # 왼쪽이 더 빠른 경우
    if target_index <= len(array) // 2:
        for i in range(target_index):
            x = array.popleft()
            array.append(x)
            cnt += 1

    # 오른쪽이 더 빠른 경우
    else:
        for i in range(len(array) - target_index):
            x = array.pop()
            array.appendleft(x)
            cnt += 1  
    array.popleft()
print(cnt)          