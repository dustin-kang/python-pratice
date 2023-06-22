# topology\_sort\_pratice

### \[실전1] 커리큘럼

<table data-header-hidden><thead><tr><th width="247.33333333333331"></th><th></th><th></th></tr></thead><tbody><tr><td><a href="../../implementation/implementation.md#메모리-제약-사항">🔗</a></td><td>시간 제한</td><td>메모리 제한</td></tr><tr><td>50분</td><td>2초</td><td>128MB</td></tr></tbody></table>

학생은 총 N개의 강의를 듣고자 한다. 모든 강의는 1번 부터 N번까지의 번호를 가지고 동시에 여러 강의를 들을 수 있으면 어떠한 강의에는 선수 강의가 있다.&#x20;

예를 들면, N=3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고 1번, 2번 강의에는 선수 강의가 없다고 가정하자. 그리고 각 강의에 대한 강 시간은 아래와 같다.

* 1번 : 30 시간
* 2번 : 20 시간
* 3번 : 40 시간

결론적으로, 3번 강의를 듣기 위한 최소 시간은 60시간이다. 학생이 듣고자 하는 N개의 강의 정보가 주어졌을 때, **N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 출력**하는 프로그램을 작성하세요.

#### 입력 조건

* 듣고 하는 강의 수 `N` 는 1 ≤ N ≤ 500입니다.
* 다음 N개의 줄에는 강의와 강의시간 그리고 강의를 듣기 위해 먼저 들어야 하는 선수 강의 번호가 자연수로 주어지며 공백으로 구분합니다. 이때 강의시간은 100,000 이하의 자연수입니다.
* 각 줄은 -1로 끝납니다.

```
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
```

#### 출력

```
10
20
14
18
17
```

### 문제 풀이

각 노드(강의)에 대해 인접 노드를 확인할 때, 인접한 노드가 현재 노드보다 더 긴 강의시간을 찾는 다면 오랜 시간 의 값을 저장하여 테이블을 갱신합니다.

```python
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]
# 각 강의별 시간은 0으로 초기화
time = [0] * (v +1)

# 방향 그래프의 간선 정보 받아오기
for i in range(1, v+1):
    data = list(map(int, input().split())
    time[i] = data[0] # 첫번 수는 시간 정보를 담고 있음
    for x in data[1:-1]: # 끝에 -1을 제외한 값은 인접 노드.
         indegree[i] += 1 # 현재 노드 진입차수 추가
         graph[x].append(i) # 선수 과목은 현재 노드와 연결
```

```python
# 위상 정렬
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    # 처음 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0: # 진입차수가 0인 노드
            q.append(i)
    
    # 큐가 빌 때 까지 반복
    while q:
        now = q.popleft()
        # 연결된 노드들의 진입 차수에서 1빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, v+1):
        print(result[i])
        
topolohy_sort()
```

위상 정렬을 통해 간선정보를 확인하여 테이블을 갱신합니다.

* result = 최종적으로 각 최소 강의 사간을 담는 리스트입니다.
* `deepcopy` 를 통해 time 리스트 변수의 값을 복사해 result 변수 값으로 설정합니다.

> 값의 연산이 있을 예정일 때, 영향을 미치지 않게 하려면 리스트 값을 복제하는  deepcopy() 함수를 이용합니다.
