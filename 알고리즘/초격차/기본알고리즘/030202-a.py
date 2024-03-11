"""
나이순 정렬

"""

n = int(input())
array = []

for i in range(n):
    age, name = input().split()
    array.append((int(age), name))

array.sort(key=lambda x : x[0])

for i in range(n):
    print(array[i][0], array[i][1])