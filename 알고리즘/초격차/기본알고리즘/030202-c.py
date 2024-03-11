"""
수 정렬하기 3
파이썬은 대략 1초에 2천만 개의 데이터를 연산할 수 있다.
But, 기본 정렬 알고리즘은 N log N

->> 계수 정렬을 사용한다.

"""

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]): # 등장 횟수 만큼 값 출력
            print(i)