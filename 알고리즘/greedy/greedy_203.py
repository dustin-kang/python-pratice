"""
1이 될때까지

-input-
25 5

-input2-
17 4
"""

def solution():
    n, k = map(int, input().split())
    count = 0

    while True:
        # 나누어 떨어지는 수가 될 때 까지 1씩 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # n이 k보다 작을 때 반복문 탈출
        if n < k:
            break
        # k로 나누기
        result += 1
        n //=k 
    
    # 마지막으로 남은 수에 대해 1씩 빼기
    result += (n-1)
    return result






    # 각 행의 숫자중 가장 큰 숫자
    return max(answer)


if __name__ == "__main__":
    print(solution())