"""
A 리스트가 [1, 3, 5]이고 B 리스트가 [2, 4, 6, 8]일 때 두 리스트를 합친 정렬 리스트를 반환하라
"""


def solution(a, b):
    answer = []
    i = 0
    j = 0

    while i < len(a) or j < len(b):
      if j >= len(b) or (i < len(a) and a[i] <= b[j]):
        answer.append(a[i])
        i += 1
      else :
        answer.append(b[j])
        j += 1
        
    
    return answer

"""
하단은 테스트 케이스
"""
import unittest

# 문제
a = [1,3,5]
b = [2,4,6,8]


# 정답
answer = [1,2,3,4,5,6,8]

class Test(unittest.TestCase):
  def test(self):
    self.assertEqual(solution(a,b), answer, msg="틀렸습니다.")

unittest.main()


