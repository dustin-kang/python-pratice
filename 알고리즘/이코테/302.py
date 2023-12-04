"""
그리디 - 곱하기 혹은 더하기

02984 -> 576
567 -> 210
"""

n = input()
result = int(n[0])
for i in range(1, len(n)):
    if int(n[i-1]) <= 1:
        result += int(n[i])
    else:
        result *= int(n[i])

print(result)









