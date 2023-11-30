"""
최단 경로 - 플로이드
A -> B 가는데 필요한 비용

5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""

INF = 1e9
n = int(input())
m = int(input())
array = [[INF] * (n+1)  for _ in range(n+1)]

# 자가 자신 -> 자기자신
for i in range(1, n+1):
    array[i][i] = 0

# 간선 정보 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    if c < array[a][b]:
        array[a][b] = c

# 플로이드 워셜 알고리즘 #
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            array[a][b] = min(array[a][b], array[a][k] + array[k][b])


# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # 도달 할 수 없는 경우 1 출력
        if array[i][j] == INF:
            print(0, end=" ")
        # 도달할 수 있는 경우 0 출력
        else:
            print(array[i][j], end=" ")
    print()

