"""
1부터 50까지의 임의의 숫자 10개가 있는 리스트 데이터를 정렬하고 
31이 있으면 "당첨"을 반환하고 없으면 "X"를 반환하는 프로그램 구현하기

반드시, "퀵정렬"과 "이진 탐색"을 사용해야 합니다.
"""

import random
class solution:
    def __init__(self):
        self.array = [random.randint(1, 50) for i in range(10)]
        self.start = 0
        self.end = len(self.array) - 1
        print(self.array)

    def sort(self, array, start, end):
        """
        ## Quick Sort Func
        > 피벗을 설정한 후 피벗 이후의 인덱스 부터 피벗보다 작으면 왼쪽 크면 오른쪽으로 이동해서 정렬하는 함수
        ### parameter
        - `array` :  정렬할 배열
        - `start` : 시작 인덱스
        - `end` : 끝 인덱스

        ### return
        X : 리스트를 정렬함.
        """
        if start >= end:
            return 
        
        pivot = start
        left = start + 1
        right = end

        while left <= right:
            while left <= end and array[left] <= array[pivot]:
                left += 1
            while right > start and array[right] >= array[pivot]:
                right -= 1

            if left > right:
                array[right], array[pivot] = array[pivot], array[right]
            else:
                array[right], array[left] = array[left], array[right]

        self.sort(array, start, right-1)
        self.sort(array, right+1, end)

    def search(self, array, target, start, end):
        """
        ## Binary Search Func
        > (start + end) // 2를 통해 중간값을 구해 중간값보다 크거나 작으면 반으로 나눠 조사한다.
        ### parameter
        - `array` :  정렬할 배열
        - `target` : 찾는 값
        - `start` : 시작 인덱스
        - `end` : 끝 인덱스

        ### return
        `target`의 인덱스를 반환하거나 존재하지 않으면 `None`을 반환
        """
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                print(self.array)
                return mid
            elif array[mid] > target:
                end = mid -1
            else:
                start = mid +1
        print(self.array)
        return None




Solution = solution()

Solution.sort(Solution.array, 0, len(Solution.array)-1)

result = Solution.search(Solution.array, 31, 0, len(Solution.array)-1)

if result == None:
    print("찾는 원소가 존재하지 않습니다.")
else:
    print(f"{result + 1}번 째 인덱스에 있습니다.")