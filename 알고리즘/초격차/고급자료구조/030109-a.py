"""
주사위
https://www.acmicpc.net/problem/1233

빈도가 높은 주사위
"""

a,b,c = map(int, input().split())

# ANSWER

counter = dict()

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            summary = i + j + k
            if summary not in counter:
                counter[summary] = 1
            else:
                counter[summary] += 1

# 가장 많이 등장한 합
max_count = -1
for (key, value) in counter.items():
    if max_count < value:
        max_count = value
        answer = key
    elif max_count == value:
        answer = min(answer, key)
print(answer)


# 1
from itertools import product

result = [0] * (max(a,b,c)*3)
multiple = product(range(1,a+1), range(1,b+1), range(1,c+1)) 
for i in list(multiple):
    result[sum(i)] +=1

print(result.index(max(result)))
    