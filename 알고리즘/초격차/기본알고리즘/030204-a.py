"""
수 정렬하기 2
https://www.acmicpc.net/problem/2751

"""
import sys
input = sys.stdin.readline

n = int(input())
array = list()

for i in range(n):
    array.append(int(input()))

array.sort() # Timsort

for i in array:
    print(i)