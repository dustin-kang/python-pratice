"""
상대적으로 전통적인 퀵정렬보다 단순한 알고리즘이지만,
피벗과 데이터를 비교하는 연산이 증가하므로 시간면에서는 비효율적이다.
하지만 기억하기 쉽다는 장점이 있다.

"""

array = [5, 7, 9, 0 , 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 담은 경우
    if len(array) >= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

