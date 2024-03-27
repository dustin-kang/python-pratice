"""
유기농 배추
DFS
https://www.acmicpc.net/problem/1012
"""
import sys
sys.setrecursionlimit(1000000) # DFS 깊이가 커질수 있기 때문에 제한하는 함수로 정상적으로 돌아가게 한다.

ts = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

B, checkk = [],[] # 농지와 방문 여부 확인
def dfs(x, y):
    global B, check
    if check[x][y] == 1:
        return
    check[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if B[nx][ny] == 0 or check[nx][ny] == 1:
            continue
        dfs(nx, ny)
    
def process():
    global B, checkk
    M,N,K = map(int, input().split())
    B = [[0 for i in range(50+2)] for _ in range(50+2)] # 농지
    check = [[0 for i in range(50+2) for _ in range(50+2)]] # 방문 여부 확인

    for _ in range(K):
        # 배추 위치를 받는다.
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1 # 배추 위치를 체크한다.
    ans = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            # 배추 위치가 아니거나 방문한적 이 있다면 넘어간다.
            if B[i][j] == 0 or check[i][j] == 1:
                continue 
            dfs(i, j)
            ans += 1
    print(ans)

for _ in range(ts):
    process()