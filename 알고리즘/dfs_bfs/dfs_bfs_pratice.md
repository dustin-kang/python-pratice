# dfs\_bfs\_pratice

> **INDEX**
>
> * [음료수 얼려먹기](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/dfs\_bfs/dfs\_bfs\_pratice.md#%EC%8B%A4%EC%A0%841-%EC%9D%8C%EB%A3%8C%EC%88%98-%EC%96%BC%EB%A0%A4%EB%A8%B9%EA%B8%B0)
> * [미로 탈출](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/dfs\_bfs/dfs\_bfs\_pratice.md#%EC%8B%A4%EC%A0%842-%EB%AF%B8%EB%A1%9C%ED%83%88%EC%B6%9C)

## \[실전1] 음료수 얼려먹기

| [🔗](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/implementation/implementation.md#%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%A0%9C%EC%95%BD-%EC%82%AC%ED%95%AD) | 시간 제한 | 메모리 제한 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------ |
| 30분                                                                                                                                                                        | 1초    | 128MB  |

N X M 개의 얼음 틀이 있을 경우, 구멍이 뚫려 있는 부분과 칸막이가 존재하는 부분은 1로 표시한다. 그리고 상하좌우가 연결되어 있는 부분을 서로 연결되어 있는 부분으로 간주한다.

이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 갯수를 구하여라.

![image](https://user-images.githubusercontent.com/55238671/236455277-4832a79a-5108-4a09-93eb-c6a381506eb9.png)

* 배열의 크기 N x M

#### 입력

```
4 5
00110
00011
11111
00000
```

#### 출력

```
3
```

### 문제 풀이

**\[DFS] 재귀함수를 이용하여 주변 지점을 살펴본 뒤에 값이 `0`이면서 해당 지점을 방문 하지 않은 지점이면 방문 한다.**

* 방문하지 않은 지점은 그대로 두고 방문한 지점은 다시 방문 할 필요 없기 때문에 `1`로 방문 처리 합니다.

```python
    if graph[x][y] == 0:
        graph[x][y] = 1 # 해당 위치 방문 처리
        # 상하좌우 위치 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False
```

**코드**

```python
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input()))) # 2차원 데이터를 입력 받음

def dfs(x,y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1 # 해당 위치 방문 처리
        # 상하좌우 위치 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for  i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
        
print(result)
```

***

## \[실전2] 미로탈출

| [🔗](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/implementation/implementation.md#%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%A0%9C%EC%95%BD-%EC%82%AC%ED%95%AD) | 시간 제한 | 메모리 제한 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------ |
| 30분                                                                                                                                                                        | 1초    | 128MB  |

N X M 크기의 직사각형 형태의 미로에 갇혀있다. 미로에는 여러마리의 괴물이 있고 탈출을 해야한다.

이떄 괴물이 있는 부분을 `0`이고 괴물이 없는 부분을 `1`이라고 할때, **탈출하기 위해 움직일 수 있는 최소 칸의 개수를 구하시오.** (시작칸과 마지막 칸을 모두 포함해야 합니다.)

![image](https://user-images.githubusercontent.com/55238671/236455317-e5edf628-fc21-4ac4-84ca-82ddf60c0016.png)

#### 입력

```
5 6
101010
111111
000001
111111
111111
```

#### 출력

```
10
```

### 문제 풀이

```python
from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input()))) # 2차원 데이터를 입력 받음

# 이동 방향 정하기 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌때 까지 반복
    while queue:
        x, y = queue.popleft() # 큐에서 빼내 다시 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or  ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx,ny)) # 큐에 카운트 추가
    return graph[n-1][m-1]


print(bfs(0,0))
```
