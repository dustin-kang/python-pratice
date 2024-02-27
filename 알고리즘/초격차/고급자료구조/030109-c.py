"""
중앙값 구하기
중상(60)
https://www.acmicpc.net/problem/2696
"""
import sys
input = sys.stdin.readline
import heapq

ts = int(input())
"""
중앙 값을 구하기 위해 원소를 하나씩 빼내서 홀수 번째에 중앙값을 확인하려면 정렬(NlogN)을 매번 해야한다는 한계가 있다.
1. 그래서 Heap을 이용해 중앙값을 기준으로 작거나 같으면 최대힙에
크면 최소힙에 넣는다.

2. 그리고 두 힙을  동일하게 맞춘다.

"""

def show_result():
    """
    정답을 출력하는 함수
    """
    print(len(result)) # 출력할 원소 개수
    for i in range(len(result)):
        print(result[i], end=' ')
        # 10개 단위로 줄바꿈
        if (i+1) % 10 == 0:
            print()
    print()

for _ in range(ts):
    m = int(input())
    data = []
    for i in range(m // 10 + 1): # 10개 단위로 입력이 들어오기 때문에
        data.extend(list(map(int, input().split())))
    left  = [] # Max Heap (최대힙은 음수 부호를 사용)
    right = [] # Min Heap 
    median = data[0]
    result = [median] # 결과 배열

    for i in range(1, m):
        # 1. 해당 값이 현재 중앙 값보다 크거나 작은경우
        if data[i] <= median: heapq.heappush(left, -data[i])
        else: heapq.heappush(right, data[i])


        # 2. 두 힙을 동일하게 맞춘다.
        if i % 2 == 0: # 동일하게 맞추기 위해 원소의 수는 짝수다.
            if len(left) > len(right): # 왼쪽에서 오른쪽
                heapq.heappush(right, median)
                median = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -median)
                median = heapq.heappop(right)   
            result.append(median)
    show_result() # 정답 출력             