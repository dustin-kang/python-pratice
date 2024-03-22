"""
등수 매기기

https://www.acmicpc.net/problem/2012
"""

# 실제 등수 : 순서
# 에상 등수 : 값

n = int(input())
array = [int(input()) for i in range(n)]
array.sort()

# 불만도 계산
result = 0

# i : 실제 등수, array[i-1] : 예상 등수
for i in range(1, len(array)+1): 
    result += abs(i - array[i-1])

print(result)