"""
보물
https://www.acmicpc.net/problem/1026

"""

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

result = 0

for i, j in zip(A, B):
    result += i * j

print(result)