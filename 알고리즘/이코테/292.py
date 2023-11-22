"""
# 최단 경로 - 미래도시


5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

3
"""

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신에서 자기자신으로 가는 비용은 0으로 처리
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 무방향 그래프, a -> b 가는 비용 설정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 가려고 하는 최종 목적지를 입력 받는다. (x 최종지점, k 중간지점)
x, k = map(int, input().split())


# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1): 
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행한 결과 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)