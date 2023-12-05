'''
이진탐색 - 고정점 찾기

5
-15 -6 1 3 7

3

7
-15 -4 2 8 9 13 15

2

'''
n = int(input())
array = list(map(int, input().split()))

def bianry_search(start, end, array):
    if start > end: # 끝 인덱스가 시작 인덱습보다 작으면 none 반환! #
        return None
    mid = (start + end) // 2

    # 고정점을 찾은 경우
    if mid == array[mid]:
        return mid
    elif array[mid] > mid:
        return bianry_search(start, mid-1, array)
    else:
        return bianry_search(mid+1, end, array)

index = bianry_search(0, n-1, array)

if index == None:
    print(-1)
else:
    print(index)