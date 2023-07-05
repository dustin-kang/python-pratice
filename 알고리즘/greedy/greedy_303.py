"""
문자열 뒤집기

0과 1로 이루어진 문자열을 뒤집기 위한 최소 횟수
 https://www.acmicpc.net/problem/1439

"""
s = input()

count0 = 0
count1 = 0

# 0으로 전부 바꾸는 것과 1로 전부 바꾸는 것 중 가장 작은 것을 선택합니다.

# 먼저 첫번째 글자가 0일 경우에 따라 다음글자가 어떤지 확인합니다.
if s[0] == '0':
    count1 += 1
else:
    count0 += 1


for i in range(len(s)-1):
    # 다음의 수가 바뀌는 경우 카운팅합니다.
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))
