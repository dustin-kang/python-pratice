> **INDEX**
> - [왕실의 나이트]()
> - [게임 개발]()


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

> 여러가지 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임입니다.

룰은 아래와 같습니다.
1. 카드들의 형태가  N * M 형태로 놓여있다.
2. 먼저 뽑고자 할 카드가 포함되어 있는 행을 선택한다.
3. 그다음, 가장 숫자가 낮은 카드를 뽑는다.
4. 따라서, 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자 카드를 뽑을 수 있게 전략을 세워라.




- 행의 갯수 N과 열의 갯수 M이 공백을 기준으로 자연수로 주어집니다. (1 <= N, M <= 100>)
- 둘째 줄 부터 N개의 줄을 걸쳐 각 카드에 적힌 숫자가 주어집니다. (1 이상 10,000 이하)


### 입력
```
3 3
3 1 2
4 1 4
2 2 2
```
```
2 4 
7 3 1 8
3 3 3 4
```
### 출력
```
2
```
```
3
```
## 문제 풀이
```python
m, n = map(int, input().split())
answer = []
for i in range(m):
    row = list(map(int, input().split()))
    answer.append(min(row))

print(max(answer))
```
