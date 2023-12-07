"""
최단 경로 - 정확한 순위

A 학생 과 B학생의 성적을 비교할 때 경로를 통해 비교한다.
- 비교가 가능하면 도달이 가능하다.

비교하는 학생 수가 500명 이하이므로 N3의 플로이드 워셜을 사용한다.

6 6
1 5
3 4
4 2
4 6
5 2
5 4

1 <= 성적을 정확히 알 수 있는 사람 수
"""

n, m = map(int, input().split())
INF = int(1e9)
graph  =[[INF] * (n + 1) for _ in range(n + 1)]

# 먼저 자기 자신에서 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0


# 각 선의 정보를 입력 받아 값을 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

print(graph)

# 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1 # 도달가능한 수
    if count == n: # 정확한 순위를 알 수 있으면(전부 도달 가능하면)
        result +=1
print(result)