"""
요세푸스 문제
30분
https://www.acmicpc.net/problem/11866
"""

from collections import deque

n, k = map(int, input().split())
answer = []
array = deque([i for i in range(1, n+1)])
cursor = 1
while array:
    if cursor == k:
        answer.append(array.popleft())
        cursor = 1
    else:           
        x = array.popleft()
        array.append(x)
        cursor += 1

# 정답 출력
print('<', end='')
for i in range(len(answer)):
    if i < len(answer) - 1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end=', ')
print('>')


"""
for i in range(n):
    for i in range(k-1):
        x = array.popleft()
        array.append(x)
    x = array.popleft()
    result.append(x)


"""
