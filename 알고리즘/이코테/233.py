"""
그리디 - 숫자 카드 게임

3 3
3 1 2 
4 1 4
2 2 2

2

2 4
7 3 1 8
3 3 3 4

3
"""


n ,m  = map(int, input().split())

result = []
for i in range(n):
    result.append(min(map(int, input().split())))

print(max(result))
