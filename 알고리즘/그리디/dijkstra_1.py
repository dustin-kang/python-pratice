import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값

# 노드의 개수(n)과 간선의 개수(m)을 받습니다.
n , m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담을 리스트를 만듭니다.
graph = [[] for i in range(n+1)]
# 방문 여부를 체크하는 리스트
visited = [False] * (n+1) 
print(visited)
# 최단 거리 테이블
distance = [INF] * (n + 1) 

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a -(c)-> b
    graph[a].append((b,c))


def get_smallest_node():
    """
    방문하지 않은 노드 중 가장 최단 거리를 찾아내 번호를 반환하는 함수
    """
    min_value = INF
    index = 0 # 인덱스 초기화
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]: # 방문한 적 없고 무한대보다 작은 경우를 첫 방문이라 하죠? -> 연결된 노드들에 해당
            min_value = distance[i] # 연결된 노드들 중 최단 경로인 노드의 인덱스를 저장
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    # 1. 연결된 노드에 값 대입 (시작의 경우)
    for j in graph[start]:
        distance[j[0]] = j[1] # 노드 연결(Next node, edge Value)

    # 2 (시작이 아닌 경우)
    for i in range(n - 1): # 마지막 단계는 변경사항이 없을 것이니 n - 1으로 설정
        # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리를 합니다.
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들 중 가장 최단의 경로 노드를 True
        
        for j in graph[now]: # 노드의 연결된 노드
            # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1] # 다음 노드의 간선 값을 구해요!
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost # 갱신!


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달 할 수 있는 거리를 출력
    else:
        print(distance[i])            



