"""
[1, 2, 3, 3, 5, 1, 6, 2] 리스트에서 연속적인 수의 합이 6인 리스트들을 반환하라
"""
data = [1, 2, 3, 3, 5, 1, 6, 2]


def solution(data):
    answer = []
    i_sum = 0
    end = 0
    num = len(data) # 끝점과 비교
    max_sum = 6 # 구간합과 비교
  
    for start in range(num):
        while i_sum < max_sum and end < num: # 구간 합보다 작은 경우
            i_sum += data[end]
            end += 1
        if i_sum == max_sum:
            answer.append(data[start:end])
        i_sum -= data[start] # 수의 합이 구간 합보다 큰 경우
    return answer

"""
하단은 테스트 케이스
"""
import unittest

# 정답
answer = [[1, 2, 3], [3, 3], [5, 1], [6]] 

class Test(unittest.TestCase):
  def test(self):
    self.assertEqual(solution(data), answer, msg="틀렸습니다.")

unittest.main()


