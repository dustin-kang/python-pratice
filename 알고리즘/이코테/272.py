"""
이진탐색 - 부품 찾기

5
8 3 7 9 2
3
5 7 9

"""

n = int(input())
array = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

array.sort()
start = 0
end = n-1

def binary_search(x, start, end):
    while start <= end: # start가 end보다 작을 때만 💡
        mid = (start + end) // 2 # 중앙 값 💡
        if x == array[mid]:
            return True
        elif x < array[mid]: # 타겟값이 중앙값보다 작은 경우 끝점 수정
            end = mid - 1
        else:
            start = mid + 1 # 타겟값이 중앙값보다 큰 경우 시작점 수정
    return False
    

for i in req:
    if binary_search(i, start, end) == True:
         print("Yes")
    else:
         print("No")

"""
이외에도 인덱스를 제품 값을 이용해 찾거나 set로 초기화하여 풀 수 있다.
"""