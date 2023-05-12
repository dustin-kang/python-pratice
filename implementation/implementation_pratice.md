> **INDEX**
> - [왕실의 나이트](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation_pratice.md#실전1-왕실의-나이트)
> - [게임 개발](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation_pratice.md#실전2-게임-개발)


# [실전1] 왕실의 나이트

왕실 정원의 크기가 8 X 8이라고 할 때, 나이트는 L자 형태(ㄱ,ㄴ)로 이동할 수 있으며, 정원 밖으로 나갈 수 없다.
1. 수평으로 두칸, 수직으로 한칸
2. 수직으로 두칸, 수평으로 한칸

그렇다면 나이트가 이동할 수 있는 경우의수는?

예를 들어, 아래 그림처럼 나이트가 c2에 있다면 경우의 수는 6가지이다.

<img width="613" alt="image" src="https://user-images.githubusercontent.com/55238671/235411395-8adc7227-3009-4266-b37d-08406e090fa1.png">



### 입력
```
a1
```
### 출력
```
2
```

## 문제 풀이
```python
# 1
# 나이트의 위치 입력 받기
data = input()
inputs = [data[0], data[1]]

count = 8 # 나이트가 이동할 수 있는 최대 경우의 수
block = ['a','1','h','8'] # 양 끝지점에 있는 위치
subblock = ['a','1','h','8', '2','b','7','g'] 

# 나이트가 해당 지점에 있을 경우 해당 수만큼 감소
for i in inputs:
    if i in subblock:
        count -= 2
        if i in block:
            count -= 1

print(count)
```

```python
# 2
# 나이트의 위치 입력 받기
data = input()
row = int(input_data[1])
col = int(ord(onput_data[0])) - int(ord('a')) + 1

step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (-1, 2), (-2, 1)] # 나이트가 이동할 수 있는 방향 8가지

result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]

    # 해당 위치로 이동이 가능할 경우에 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
```

<img width="676" alt="image" src="https://user-images.githubusercontent.com/55238671/235411435-cfabcdcc-525a-43d8-92a7-17bba78b13bd.png">


앞 [상하좌우](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/implementation/implementation.md#-상하좌우) 문제에서는 `dx,dy` 리스트를 선언하여 이동 방향을 기록 하였고 이번에는 `steps` 변수가 dx와 dy의 기능을 대신하여 사용한다.


---

# [실전2] 게임 개발

게임 캐릭터가 맵  안에서 움직이는 시스템을 개발해야 한다.

<img width="288" alt="image" src="https://user-images.githubusercontent.com/55238671/235599450-2e2f8f9d-881c-4128-8540-a7c00811d79a.png">


맵의 크기는 `N x M`의 크기 직사각형으로, 캐릭터는 동서남북 중 한 곳만 바라본다.
캐릭터는 상하좌우로 움직일 수 있고 바다로 되어 있는 공간엔 갈 수 없다.
아래는 캐릭터의 움직임 설정 메뉴얼이다.

```
1. 현재 위치에서 현재 방향 기준으로 왼쪽부터 차례대로 갈 곳을 정한다.
2. 
    2-1. 캐릭터의 왼쪽 방향에 아직 가보지 않은 칸이 있다면, 왼쪽 방향으로 회전한다음, 왼쪽으로 한칸 전진
    2-2. 캐릭터의 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전한 다음, 1번으로 돌아간다.
3. 만약 네방향 모두가 가본 칸이거나 바다라면 바라보는 방향을 유지한 채 한 칸 뒤로 가고 1단계로 돌아온다. 이때 뒤 방향이 바다라면 움직임을 멈춘다.

- 북(0), 동(1), 남(2), 서(3)
```

### 입력
```py
4 4 # 4 x 4 맵
1 1 0 # (1,1)에 0(북쪽 방향)을 바로보고 서 있는 캐릭터
1 1 1 1 # 1: 바다 # 0: 육지
1 0 0 1
1 1 0 1 
1 1 1 1
```

### 출력
```
3
```

## 문제 풀이
### 1. 캐릭터 위치와 맵 리스트로 입력 받기
```python
m , n = map(int, input().split())

d  = [[0] * m for _ in range(n)] # 방문한 위치

x, y, direction = map(int, input().split()) # 캐릭터 위치
d[x][y] = 1 # 현재 방문 위치 표시

# 전체 맵 정보 받기
array = []
for _ in range(n):
    array.append(list(map(int, input().split()))) 

# ⭐️ 북 동 남 서 방향으로 방향 정의 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
```

### 2. 왼쪽으로 회전의 경우 함수 작성
```python
def turn_left():
    global direction
    direction -= 1 # 방향이 서쪽(-1)인 경우 3으로 바꾸기, -1에서 가감하면 끝없기 때문
    if direction == -1:
        direction = 3
```

### 3. 시뮬레이션
```python
# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1 # 방향이 서쪽(-1)인 경우 3으로 바꾸기, -1에서 가감하면 끝없기 때문
    if direction == -1:
        direction = 3


count = 1 # 방문 수
turn_time = 0 # 회전 max : 4
while True:
    # 2번
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    # 2-1
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 2-2
    else: 
        turn_time += 1
    # 3
    if turn_time == 4: # 한바퀴 다 회전 했을 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else :
            break
        turn_time = 0

print(count)
```
