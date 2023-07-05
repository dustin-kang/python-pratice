"""
곱하기 혹은 더하기
<문제 해석>
'x','+'를 각 숫자 중간에 넣어 만들 수 있는 최대 수를 구하여라
- 각자리수는 0부터 9까지
- 순서대로 01234 => 0 + 1 X 2 X 3 X 4
"""

# 문제 풀이

n = str(input())
answer = int(n[0])
for i in range(1, len(n)):
    if int(n[i]) in (0, 1) or int(n[i-1]) in (0, 1): # 현재 숫자와 이전 숫자가 0 아니면 1일 경우 더하기
        answer += int(n[i])
    else: # 아니면 곱셈
        answer *= int(n[i])

print(answer)

# 정답
# 두 수중 하나라도 1이하에 경우 더하기를 하면 된다.

data = input()

result = int(data[0]) # 첫번쨰 원소의 값

# 두번째 원소부터 마지막 원소 까지, 0일 경우에만 더하기 진행
for i in range(1, len(data)): 
    num = int(data[i])
    if num <= 1 and result <= 1: # 두수 중 하나라도 0 혹은 1인 경우 곱하기보다 더하기가 효율적
        result += num
    else:
        result *= num
print(result)