"""
이진탐색 - 정렬된 배열에서 특정 수의 개수 구하기

7 2
1 1 2 2 2 2 3

-> 4

7 4
1 1 2 2 2 2 3

-> -1

- 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.
"""

# 2-a
def search_a(x, start, end):
    mid = (start + end) // 2

    if x == lst[mid] and start != end:
        global result
        result += 1
        search_a(x, start, mid)
        search_a(x, mid+1, end)
        return result
    elif x > lst[mid] and mid < end:
        search_a(x, mid+1, end)
    elif x < lst[mid] and mid < end:
        search_a(x, mid+1, end)        
    else:
        pass

# 2-b
def search_b(lst, x):
    n = len(lst)

    a = first(lst, x, 0, n-1)
    
    if a == None: 
        # 존재하지 않는 경우
        return 0
    
    b = last(lst, x, 0, n-1)

    return  b - a + 1

def first(lst, x, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # 해당 값을 가지고 있는 가장 왼쪽에 있는 인덱스 변환
    if (mid == 0 or x > lst[mid-1]) and lst[mid] == x:
        return mid
    
    elif lst[mid] >= x:
        # x보다 값이 작거나 같은 경우
        return first(lst, x, start, mid-1)
    else:
        # x보다 값이 큰 경우
        return first(lst, x, mid + 1, end)
    
def last(lst, x, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # 해당 값을 가지고 있는 가장 오른쪽에 있는 인덱스 변환
    if (mid == n -1 or x < lst[mid-1]) and lst[mid] == x:
        return mid
    elif lst[mid] > x:
        return last(lst, x, start, mid-1)
    else:
        return last(lst, x, mid+1, end)

# 2-c. bisect를 이용한 문제풀이
# 참고 https://github.com/dongwoodev/CodingTest/blob/Python/파이썬기초/Pythoncode.ipynb 
from bisect import bisect_left, bisect_right

def search_c(lst, left_value, right_value):
    right_index = bisect_right(lst, right_value)
    left_index = bisect_left(lst, left_value)
    return right_index - left_index



# 0. 기본 값 대입
n, x = map(int, input().split())
lst = list(map(int, input().split()))
result = 0


start, end = 0, n-1
# 2-a. 이진 탐색 풀이
count = search_a(x, start, end)

# 2-b. 두개의 이진 탐색으로 첫위지와 마지막 위치를 찾기
count = search_b(lst, x, start=0, end=n-1)

# 2-c. bisect를 이용한 문제풀이
count = search_c(lst, x, x)

# 2. 원소 존재 여부 개수 확인
if count == 0:
    print(-1)
else:
    print(count)


