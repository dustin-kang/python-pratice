# 그리디 - 모험가 길드
"""
그리디 - 모험가 길드
5
2 3 1 2 2
"""


n  = int(input()) # 5명의 용사들
lsts = list(map(int, input().split()))
lsts.sort(reverse = True)
# 3 2 2 2 1

result = 0

for i in lsts: # 공포도가 큰 순서대로 반복
    if n <= 0:
        # 총 인원이 0보다 작거나 같으면 BREAK
        break
    n = n - i # 가장 공포도가 높은 사람만큼 뺀다. (공포도 is 팀 맴버)
    result += 1

print(result)