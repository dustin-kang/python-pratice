"""
금광

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

19
16
"""

t = int(input())

while t > 0:
    n ,m  = map(int, input().split())
    array = list(map(int, input().split()))

    dp_table = []
    index = 0

    # DB 테이블 2차원 배열 만들기
    for i in range(n):
        dp_table.append(array[index:index+m]) # [[1, 3, 3, 2], [2,1,4, 1] ...
        index += m 


    for j in range(1, m): # 1,2,3 (2번째 열부터 )
        for i in range(n): # 0, 1, 2(0번째 행 ~)
            # 왼쪽 위에서 오는 경우
            if i == 0: # 첫 행일 때 왼쪽위에서 올 수 없음
                left_up = 0
            else: 
                left_up = dp_table[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: # 마지막 행(2)일때 왼쪽 아래에서 올 수 없음
                left_down = 0
            else: 
                left_down = dp_table[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp_table[i][j - 1]
            
            # 현재 금광의 값과 이전 왼쪽위, 왼쪽, 왼쪽아래에서 오는 값들 중 최댓값의 합
            dp_table[i][j] = dp_table[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n): # 0, 1, 2
        result = max(result, dp_table[i][m-1]) # 14, 13, 19중 최대 값
    
    print(result)
    t -= 1 # 2번째 반복