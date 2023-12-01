"""
그래프 - 커리큘럼
- 듣고자 하는 강의 수
- 각 강의당 강의 시간과 먼저 들어야 하는 강의 번호
- -1은 줄을 구분하기위한 숫자다.


10 - 10
   - 4  - 3
   --- -- 4

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""

from collections import deque
import copy # time을 복사해 결과를 담을 리스트 생성(id는 다름)

v = int(input()) # 노드의 개수
indegree = [0] * (v+1) # 모든 노드에 대한 진입 차수를 0으로 초기화 #
graph = [[] for i in range(v+1)]
time = [0] * (v+1) # 각 강의 시간을 0으로 초기화


# 방향 그래프의 모든 간선 정보를 입력 받는다.
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫번째 데이터는 시간 정보를 담음
    for x in data[1:-1]: # 선수 강의 들의 대한 정보는 진입 차수에 담음
        indegree[i] += 1
        graph[x].append(i)

# graph = [[], [2, 3, 4], [], [4, 5], [], []] # 노드에 연결된 간선 정보
# indegree = [0, 0, 1, 1, 2, 1] # 연결된 진입 차수 개수
# time = [0, 10, 10, 4, 4, 3] # 각 강의 당 시간

# 위상 정렬
def topology_sort():
    result = copy.deepcopy(time) # result = time
    q = deque()

    # 진입 차수가 0이라면(초기노드) 큐에 넣는다.
    for i in range(1, v+1):
        if indegree[i] == 0:
            # 1번째 노드
            q.append(i)

    # 초기노드를 꺼내 빌때까지 반복
    while q:
        now = q.popleft()

        # 해당 노드와 연결된 노드들의 진입차수에서 1씩 빼기
        for i in graph[now]: # 2, 3, 4
            # print(i, result[i], result[now]+time[i])
            result[i] = max(result[i], result[now]+time[i]) # 현재보다 강의시간이 긴 경우 저장 (10(현재), 20(1->2))
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()




