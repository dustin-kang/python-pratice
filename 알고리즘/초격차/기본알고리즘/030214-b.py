"""
뒤집기

https://www.acmicpc.net/problem/1439
"""

a = input()
count0 = 0 # 전부 0으로 만드는 경우
count1 = 0 # 전부 1로 만드는 경우

if a[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        if a[i + 1] == '1':
            count0 += 1 # 1로 바꾸는 경우
        else:
            count1 += 1 # 0으로 바꾸는 경우

print(min(count0, count1))