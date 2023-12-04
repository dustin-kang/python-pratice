"""
DFS/BFS - 연구소
1. dfs(0), dfs(1) dfs(2) 순으로 재귀적으로 울타리 설치
2. 울타리 개수가 3개가 되면 temp에 복사해 바이러스 감염 진행
3. 진행됬을 때 0의 개수와 이전 0의 개수를 비교하여 최대값 갱신
4. 다시 dfs를 이용해 울타리 탐색


7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

9
"""

n, m = map(int, input().split())

graph = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 감염할 임시 맵

for i in range(n):
        graph[i] = list(map(int, input().split()))


# 바이러스 감염 #
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def virus(x, y):
    """
    ## 바이러스 감염 함수
    상하좌우 방향으로 감염을 시키고 재귀적으로 다음 위치(nx, ny)로 이동
    """
    for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]

          if nx >=0  and  nx < n and ny >=0 and ny < n:
                if temp[nx][ny] == 0:
                      temp[nx][ny] = 2
                      virus(nx, ny)

def get_score():
    """
    ## 안전 구역 크기 계산
    """
    score = 0
    for i in range(n):
        for j in range(m):
               if temp[i][j] == 0:
                    score += 1
    return score

result = 0
def dfs(count):
    """
    울타리를 재귀적으로 설치하면서
    위 안전 구역 크기 계산(get_score)
    """
    global result
    if count == 3:
        # 울타리가 3개가 된 경우, temp에 덮어 씌우고 감염 진행후 남는 안전 구역 크기 계산
        for i in range(n):
             for j in range(m):
                  temp[i][j] = graph[i][j]
        
        # 감염 진행
        for i in range(n):
             for j in range(m):
                  if temp[i][j] == 2:
                       virus(i, j)

        result = max(result, get_score()) # 0의 개수 파악후 갱신
        return

    for i in range(n):
         for j in range(m):
              if graph[i][j] == 0:
                   graph[i][j] = 1
                   count += 1
                   dfs(count)
                   # 끝나면 해당 위치를 0으로 바꾸고 다시 이동하기
                   graph[i][j] = 0
                   count -= 1

dfs(0)
print(result)
