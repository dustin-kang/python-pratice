"""
이진 탐색 - 떡볶이 떡 만들기

4 6
19 15 10 17

15
"""

n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start, end = 0, max(array)

# 이진 탐색
def binary_search(start, end, m):
    result = 0 # 떡들의 합 초기화
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                total += (x - mid) # 자른 떡들의 합이 6보다 작아야함.

        # 떡이 부족한 경우
        if total < m:
            end = mid - 1 # 끝 점을 줄이고 다시 자르기(while) 
         # 떡이 충분히 많은 경우
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답 
            start = mid + 1 # 시작점을 높이고 다시 자르기(while)
    return result

print(binary_search(start, end, m))