"""
구현 - 왕실의 나이트

a1
"""

result = 0
# 먼저, 해당 말의 위치를 입력받습니다.
inputs = input()
r = int(inputs[1]) # 1
c = ord(inputs[0]) - 96 # a

steps = [(-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)] # 최대 경우의 수를 알아냅니다.

# 만약 해당 경우의수가 정원 밖에 벗어나면 패스
for step in steps:
    if step[0] + c <= 0 or step[1] + r <= 0 or step[0] + c > 8 or step[1] + r < 8:
        pass
    else:
        result += 1

print(result)