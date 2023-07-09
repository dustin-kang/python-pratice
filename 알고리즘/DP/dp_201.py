"""
1로 만들기

정수 X를 아래 연산 4개를 사용하여 1을 만든다고 할때 
최소 연산을 사용하는 횟수를 구하여라

- 5로 나누어 떨어지면 5로 나눈다
- 3으로 나누어 떨어지면 3으로 나눈다
- 2로 나누어 떨어지면 2로 나눈다
- 1로 나누어 떨어지면 1로 나눈다

-input-
26

-output
3
"""

x = int(input())

memo = [0] * 300001

for i in range(2, x+1):
    memo[i] = memo[i - 1] + 1 # 함수의 호출을 위해 끝에 1을 더해줍니다.
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1) # 현재 연산, 이전 연산 + 1
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1) 
    if i % 5 == 0:
        memo[i] = min(memo[i], memo[i // 5] + 1)
print(memo[x])


