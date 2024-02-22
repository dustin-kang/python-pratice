"""
풍선 떠트리기
https://www.acmicpc.net/problem/2346
"""
from collections import deque

n = int(input())
array = list(map(int, input().split()))
array = deque([(value, idx) for idx, value in enumerate(array)])

answer = [0] * n

ball = 1
while array:
    num, idx = array.popleft()
    answer[idx] = ball
    ball += 1

    if not array:
        break

    if num > 0:
        # 양수
        for i in range(num - 1):
            temp = array.popleft()
            array.append(temp)
    else:
        # 음수
        num = abs(num)
        for i in range(num):
            temp = array.pop()
            array.appendleft(temp)

print(answer)



    

    
    

