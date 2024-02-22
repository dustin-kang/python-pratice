"""
스택
20분
https://www.acmicpc.net/problem/10828

"""
import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    command = input().strip().split() # 공백 기준 구분  ✨strip()

    # 원소 삽입
    if command[0] == "push":
        array.append(int(command[1]))
    
    # 원소 삭제
    elif command[0] == 'pop':
        if len(array) == 0: print(-1)
        else: print(array.pop())

    # 원소 최상단 출력
    elif command[0] == 'top':
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])

    # 원소의 개수
    elif command[0] == 'size':
        print(len(array))

    # 스택이 비어있는지 여부(empty)
    else:
        if len(array) == 0:
            print(1)
        else:
            print(0)