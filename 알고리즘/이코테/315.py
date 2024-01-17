"""
DFS/BFS - 특정 거리 도시찾기

4 4 2 1
1 2
1 3
2 3
2 4

-> 4
"""

"""
먼저 그래프를 2차원 배열로 만든다.
그다음 방문을 체크하기 위한 배열과 스택 배열을 생성한다.
기존 x는 이미 방문을 한 상황이기 때문에 0으로 처리한다.

이제 방문을 하나씩한다.
스택에 넣어둔 첫 노드를 꺼내 이어진 노드들을 하나씩 가져온다.
가져온 노드들의 방문이 첫방문인 경우에 거리를 +1 추가한다.
그다음 다시 이어진 노드들을 스택에 넣고 (스택이 빌 때까지 )반복한다.

"""

n, m, k, x = map(int, input().split()) #도시, 도로, 특정 거리, 시작점

# 💡 2차원 배열 만들기
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b  = map(int, input().split())
    graph[a].append(b)



# 💡 어떻게 하면 거리가 k일 때 멈출 수 있을까?
# -> 모든 도시의 최단 거리 리스트를 만들어 탐색할 때 마다 1씩 증가한다.

def dfs(x, graph):
    stack = []
    stack.append(x)
    # 모든 도시의 최단 거리 초기화
    distance = [-1] * (n+1)
    distance[x] = 0
    
    while stack:
        node = stack.pop()

        for next_node in graph[node]:
            if distance[next_node] == -1: # 방문하는 노드가 처음 방문 하는 경우
                distance[next_node] = distance[node] + 1
                stack.append(next_node)

    return distance

check = False
result = dfs(x, graph)
for i in range(1, n+1):
    if result[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)