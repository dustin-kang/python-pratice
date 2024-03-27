"""
시리얼 번호
https://www.acmicpc.net/problem/1431

연산 최대 2500

1. 길이
2. 자리수의 합이 작은 것이 먼저
3. 사전순
"""

n = int(input())

array = []
for i in range(n):
    serial = input()
    serial_int = 0
    for j in serial:
        if j.isdigit():
            serial_int += int(j)

    array.append((serial, serial_int , len(serial)))

array.sort(key= lambda x: (x[2], x[1], x[0]))

for i in range(n):
    print(array[i][0])
