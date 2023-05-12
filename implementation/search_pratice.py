# 반복문으로 구현했을 경우
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 재귀함수로 구현한 경우
def binary_search_recursion(array, target, start, end):
    # 정렬이 되어있지 않은 경우
    if start > end:
        return None 
    
    mid = (start + end) // 2 # 중간점 반환
    
    # 찾고자 하는 데이터가 중간값, 중간 초과, 중간 미만 일 경우
    if array[mid] == target: 
        return mid
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid-1)
    else:
        return binary_search_recursion(array, target, mid + 1, end)

result = binary_search([], 7, 0, 9)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)