"""
구현 - 게임 개발

4 4
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1

-> 3


- 1 : 바다, 0 : 육지
- 1, 1, 0 : (1,1)에 0(북쪽 : 북동남서 +=1)
"""



n, m = map(int, input().split())
dx, dy, dirs = map(int, input().split())
result = 1
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

maps = [list(map(int, input().split())) for _ in range(n)]
maps[dx][dy] = 1 # 현재 위치는 방문 처리

def left():
    """
    -90도 회전
    """
    global dirs
    dirs -= 1
    if dirs == -1:
        dirs = 3

turn_time = 0

while True:
    left() # 1. 왼쪽 회전

    # 2. 다음 좌표 설정
    x, y = directions[dirs]
    nx = dx + x
    ny = dy + y

    # 3. 다음 좌표가 0인 경우 아닌 경우로 나눔
    if maps[nx][ny] == 0:
        maps[nx][ny] = 1
        dx = nx
        dy = ny
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1 # 아닌 경우 +1 하여 방향을 바꿈
    
    # 네 방향 모두 막혀 있는 경우
    if turn_time == 4:
        nx = dx - x
        ny = dy - y
        # 뒤로 갈 수 있는 지 확인
        if maps[nx][ny] == 0:
            dx = nx
            dy = ny
        else:
            break
        turn_time = 0

print(result)