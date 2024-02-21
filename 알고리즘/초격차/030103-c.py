"""
스택 수열
30분
https://www.acmicpc.net/problem/1874
"""
import sys
input = sys.stdin.readline

n = int(input())

stack = []
answer = []
current = 1

for _ in range(n):
    x = int(input())
    while len(stack) == 0 or stack[-1] < x:
        # 해당 스택이 비었거나 x가 더 큰 경우 원소를 삽입
        stack.append(current)
        current +=1
        answer.append('+')
    
    # 만약 top()과 x가 동일하다면, 스택에서 제거
    if stack[-1] == x:
        answer.append('-')
    else:
    # 만약 스택의 top()보다 x가 더 작다면 해당 수열을 만드는 것은 불가능하다.
        answer = ['NO']
        break

for x in answer:
    print(x)
