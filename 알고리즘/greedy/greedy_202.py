"""
숫자 카드 게임

-input 1-
3 3
3 1 2
4 1 4
2 2 2

-input 2-
2 4 
7 3 1 8
3 3 3 4
"""

def solution():
    m,n = map(int, input().split())
    answer = []
    for i in range(m):
        # row : 해당 행에 가장 낮은 숫자
        row = list(map(int, input().split()))
        answer.append(min(row))

    # 각 행의 숫자중 가장 큰 숫자
    return max(answer)


if __name__ == "__main__":
    print(solution())