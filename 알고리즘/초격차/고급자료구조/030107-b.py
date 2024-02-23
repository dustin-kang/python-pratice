"""
이중 우선순위 큐
중상(60분)
https://www.acmicpc.net/problem/7662

"""

import sys, heapq
input = sys.stdin.readline

def pop(heap):
    """
    ### 최대힙과 최소 힙 싱크 맞추기
    #### 삭제 여부 체크 함수로 데이터를 `pop` 하면 그 데이터는 삭제 `True`로 변경
    #### 만약 데이터가 존재하지 않는 경우 `None` 반환
    - 우선순위가 높은 것을 삭제할 때 최대힙에서 빼고 최소 힙과 싱크를 맞춘다.
    - 별도의 번호(ID) 값으로 삭제 여부(이미 지워졌는지)를 기록한다.(num, j)
    - 나중에 데이터를 뺄 때 이미 삭제된 데이터라면 한번 더 뽑는다.
    """
    while len(heap) > 0:
        # 삭제할 원소가 나올떄 까지 반복
        data, id = heapq.heappop(heap)
        if not deleted[id]: # 해당 값이 False가 아니면
            deleted[id] = True 
            return data
    return None


for i in range(int(input())):
    k = int(input())
    max_q = [] # 최대 힙
    min_q = [] # 최소 힙

    # 중요한 건, 두 힙의 ✨싱크✨를 맞춰주는 게 관건!
    current = 0 # 삽입할 원소의 인덱스
    deleted = [False] * (k+1) # 원소만큼 두어 삭제 여부를 확인한다.

    for j in range(k):
        command = input().split()
        operator, data = command[0], int(command[1])

        if operator == 'I':
            # 정수 삽입
            heapq.heappush(min_q, (data, current))
            heapq.heappush(max_q, (-data, current))
            current += 1

        if operator == 'D':
            if data == -1:
                # 최소값 삭제
                pop(min_q)
            else:
                # 최대값 삭제
                pop(max_q)
    
    max_value = pop(max_q)
    if max_value == None : print("EMPTY")
    else:
        # max_q에서 값을 꺼냈다면 min_q에서도 꺼내는 것과 마찬가지
        heapq.heappush(min_q, (-max_value, current))
        print(-max_value, pop(min_q))



