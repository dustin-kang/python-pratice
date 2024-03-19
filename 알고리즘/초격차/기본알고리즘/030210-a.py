"""
LCS (최장공통부분수열)
: 공통 부분 수열 중 가장 긴 것
https://www.acmicpc.net/problem/9251

<입력, 최대 1,000글자>
ACAYKP
CAPCAK

<출력, ACAK>
4
"""

a, b = input(), input()
LCS = [[0]* (len(b)+1) for _ in range(len(a)+1)] # 초기 테이블

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        # if i == 0 or j == 0: # 마진 설정
        #     LCS[i][j] = 1
        if a[i-1] == b[j-1]: # 문자가 같은 경우
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else: # 그렇지 않은 경우
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])


print(LCS[len(a)][len(b)])