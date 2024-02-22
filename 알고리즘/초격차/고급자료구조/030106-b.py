"""
수 찾기
https://www.acmicpc.net/problem/1920
"""

a = int(input())
array = set(map(int, input().split())) 
# set 자료형을 이용하면 간단하게 이용할 수 있다.
# 주로 특정 원소를 찾을 때 사용한다.

b = int(input())
brray = list(map(int, input().split()))

for i in brray:
    if i not in array:
        print('0')
    else:
        print('1')