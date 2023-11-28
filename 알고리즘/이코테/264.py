"""
정렬 - K번 바꿔치기로 두배열 원소 교체

5 3
1 2 5 4 3
5 5 6 6 5

26
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 1 2 3 4 5
b.sort(reverse=True) # 6 6 5 5 5

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # swap
    else:
        break

print(sum(a)) # 6 6 5 4 5 = 26
