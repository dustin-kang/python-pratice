"""
제로
20분

https://www.acmicpc.net/problem/10773
"""

k = int(input())
array = []

for _ in range(k):
    number = int(input())
    if number == 0:
        array.pop()
    else:
        array.append(number)

print(sum(array))