"""
큰수의 법칙

-input-
5 8 3
2 4 5 4 6
"""

def solution():
    n, m, k = map(int, input().split(" "))
    array = list(map(int, input().split(" ")))

    # 배열을 정렬한 다음, 가장 큰 수를 카운팅
    # 만약 카운팅이 가득차면 두번째 큰 수로 삽입하고 카운팅 초기화
    
    array.sort()
    count = 0
    answer = 0


    while m > 0:
        if count == k:
            count = 0
            m -= 1
            answer += array[-2]
        else:
            count += 1
            m -= 1
            answer += array[-1]

    return answer




if __name__ == "__main__":
    print(solution())