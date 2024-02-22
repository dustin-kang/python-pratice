"""
음계 
https://www.acmicpc.net/problem/2920

"""

array = list(map(int, input().split()))

a = True
d = True

for i in range(1, len(array)):
    if array[i] > array[i-1]:
        d = False
    elif array[i] < array[i-1]:
        a = False

if a:
    print("ascending")
elif d:
    print("descending")
else:
    print('mixed')