"""
강의실
중(50분)
https://www.acmicpc.net/problem/1374
"""
import heapq

n = int(input()) # 강의 개수

lecture_list = []
for _ in range(n):
    """
    강의 시작 시간을 기준으로 강의목록(lecture_list)에 넣는다.
    우선순위큐를 사용하면 자동으로 시작시간 기준으로 정렬된다.
    """
    order,start,end = map(int, input().split())
    heapq.heappush(lecture_list, (start, end))

"""
배정된 강의실을 처리하기 위해 우선순위 큐를 생성한다.
강의시간이 겹치면 새로운 강의가 필요하고
그렇지 않으면 기존 강의실에서 새로운 강의를 배치하면 된다.

이때, 새 강의의 시작시간과 현재 강의들의 종료 시간을 비교하면 된다.
"""

lecture_placed = []
start, end = heapq.heappop(lecture_list)
heapq.heappush(lecture_placed, end)
count = 1

for _ in range(1, n):
    # 새로운 강의 꺼내기
    new_start, new_end = heapq.heappop(lecture_list)
    # 기존 강의 꺼내기(가장 일찍 끝나는)
    end = heapq.heappop(lecture_placed)

    if new_start < end:
       # 강의 시간이 겹친다.
       heapq.heappush(lecture_placed, end)
       heapq.heappush(lecture_placed, new_end)
       count += 1
    else:
       # 강의 시간이 겹치지 않는다.
       heapq.heappush(lecture_placed, end)

print(count)