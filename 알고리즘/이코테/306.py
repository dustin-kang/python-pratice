"""
그리디 - 무지의 먹방 라이브
https://school.programmers.co.kr/learn/courses/30/lessons/42891

-> 가장 적은 시간의 음식부터 뺴면서 k 시간이 됬을 때 다음 번호  음식 출력
그래야 효율성있게 문제를 풀 수 있음
"""

import heapq # 우선순위 큐를 위함

def solution(food_times, k):
    answer = 0
    
    # 전체 음식을 먹는것 보다 K가 크거나 같은 경우
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호)
        heapq.heappush(q, (food_times[i], i+1)) 
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수
    
    # sum_value + (현재 음식시간 - 이전 음식 시간) * 현재 남은 음식 개수 <= k
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 가장 적은 시간 순서대로 뽑음
        sum_value += (now - previous) * length # 3 -> 5(+2)
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중 몇번째 음식인지 출력
    answer = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return answer[(k - sum_value) % length][1] # 그 다음에 올 음식의 번호 출력

assert solution([3,1,2], 5) == 1
assert solution([8,6,4], 15) == 2