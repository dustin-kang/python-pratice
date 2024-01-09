"""
뱀
https://www.acmicpc.net/problem/3190
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

9
"""
n = int(input())
board = [[0] * (n+1) for _ in range(n +1)]

# 사과
for apple in range(int(input())):
    x, y = map(int, input().split())
    board[x][y] = 1

# 뱀
dx = [0, 1, 0, -1] # 동남서북
dy = [1, 0, -1, 0]

info = []
for snake in range(int(input())):
    x, c = input().split()
    info.append((int(x), c))

def turn(direction, c):
    # 좌측 회전의 경우
    if c == "L":
        direction = (direction - 1) % 4
    # 우측 회전의 경우
    else:
        direction = (direction + 1) % 4
    return direction
 
def simulate():
    sx, sy = 1, 1 # 뱀 위치
    board[sx][sy] = 2 
    direction = 0
    time = 0
    index = 0
    q = [(sx, sy)] # 뱀의 차지하고 있는 위치 정보

    while True:
        nx = sx + dx[direction]
        ny = sy + dy[direction]
        
        # board 내에 있고 해당위치가 뱀이 차지하고 있는 위치가 아닌 경우
        if 1 <= nx and nx <= n and 1<= ny and ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                # 사과(1)의 위치가 아닌 경우
                board[nx][ny] = 2
                q.append((nx, ny))
                ## 꼬리 제거
                tx, ty = q.pop(0)
                board[tx][ty] = 0
            else:
                # 사과의 위치가 맞는 경우
                board[nx][ny] = 2
                q.append((nx,ny))
        else:
            #board 밖에 벗어난 경우
            time += 1
            break
        
        sx, sy = nx, ny # 다음 위치로 이동
        time += 1
        if index < 1 and time == info[index][0]:
            # 회전 해야하는 경우 회전하기
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
