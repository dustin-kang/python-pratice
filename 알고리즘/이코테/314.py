"""
외벽 점검
https://school.programmers.co.kr/learn/courses/30/lessons/60062
투입해야하는 친구 수의 최솟값 반환

"""

from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    # 길이를 2배 늘려 원형을 일자 형태로 변경 [1, 5, 6, 10, 13, 17, 18, 22]
    for i in range(length):
        weak.append(weak[i] + n) 
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            # firends : 친구들을 나열하는 모든 경우의 수 (1,2,3,4) (1,2,4,3)...
            count = 1
            position = weak[start] + friends[count - 1]
            # 시작 지점부터 모든 취약 지점 확인
            for index in range(start, start+length):
                # 점검 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구 트입
                    if count > len(dist): # 더 투입이 불가능하면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최소값 계산
    if answer > len(dist):
        return -1
    return answer