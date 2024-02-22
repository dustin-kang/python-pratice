"""
나는 요리사다
https://www.acmicpc.net/problem/2953
"""

cook = []
for i in range(1, 6):
    m = sum(map(int, input().split()))
    cook.append((i, m))
    
cook.sort(key= lambda x : -x[1])
print(f"{cook[0][0]} {cook[0][1]}")
