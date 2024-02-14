"""
다이나믹 프로그래밍

편집 거리 : a를 b로 만들기 위해 사용한 연산의 수
문자열 a를 b로 바꾸는다고 했을 때 세 연산 중 한번에 하나씩 선택해 이용
- insert : 특정 위치에 문자 하나 삽입
- remove : 특정 위치에 문자 하나 삭제
- replace : 특정 위치에 문자 하나 교체

이때 최소 편집 거리를 계산하시오.

1 <= 문자열의 길이 <= 5000


cat
cut

1

sunday
saturday
3
"""

def edit_dist(str1, str2):
    """
    ### 최소 편집 거리를 구하려면 2차원 테이블로 만들어 구해야한다.
    1. 행과 열에 해당 문자가 동일한 경우 : 왼쪽 위에 수 그대로 삽입
        `dp[i][j] = dp[i-1][j-1]`
    2. 행과 열에 해당 문자가 다른 경우 : 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중 가장 작은수에서 1을 더함
        `dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])`
    """

    # a(행) x b(열)로 2차원 테이블을 만든다.
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 빈문자열에서 "saturday"를 채우기 위해 8글자가 필요하므로 초기화한다.
    for i in range(1, n+1): # sunday
        dp[i][0] = i
    for j in range(1, m+1): # saturday
        dp[0][j] = j

    # 이번엔 점화식 대로 차례대로 해당 수를 대입하면 된다.
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같은 경우, 왼쪽 위에 해당하는 수 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]

# 문자열 입력받기
str1 = input()
str2 = input()

print(edit_dist(str1, str2))
