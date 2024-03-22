"""
거스름돈

https://www.acmicpc.net/problem/5585
"""

taro = 1000 - int(input())
count = 0 

for i in [500, 100, 50, 10, 5, 1]:
    count += taro // i
    taro %= i

print(count)
