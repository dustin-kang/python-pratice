> **INDEX**
> - [실전 문제 : 1로 만들기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전1-1로-만들기)
> - [실전 문제 : 개미 전사](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전2-개미-전사)
> - [실전 문제 : 바닥공사](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전3-바닥-공사)
> - [실전 문제 : 효율적인 화폐 구성](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전4-효율적인-화폐-구성)


# [실전1] 1로 만들기

|[🔗](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation.md#메모리-제약-사항)|시간 제한|메모리 제한|
|---|---|---|
|20분|1초|128MB|

정수 X가 주어졌을 때, 연산 4개를 사용해서 1를 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

1. X가 5로 나누어 떨어지면 5로 나눈다.
2. X가 3으로 나누어 떨어지면 3으로 나눈다.
3. X가 2로 나누어 떨어지면 2로 나눈다.
4. X가 1로 나누어 떨어지면 1로 나눈다.

- 첫째 줄에 정수 X가 주어진다. (1 <= X <= 30,000)

### 입력
```
26
```
### 출력
```
3
```


#### 코드
이 문제는 동일한 함수를 구하는 값들을 동일하게 사용할 수 있다.
- 끝에 1을 더해주는 이유는 함수의 호출 횟수를 구해야 하기 때문이다.
```python
 x = int(input())

memo = [0] * 300001 # DP 테이블 초기화

for i in range(2, x+1):
    memo[i] = memo[i - 1] + 1 # 현재의 수에서 1을 뺴는 경우

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1) # 최소값

    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1) # 최소값

    if i % 5 == 0:
        memo[i] = min(memo[i], memo[i // 5] + 1) # 최소값

print(memo[x])   
```

---

# [실전2] 개미 전사

|[🔗](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation.md#메모리-제약-사항)|시간 제한|메모리 제한|
|---|---|---|
|30분|1초|128MB|

개미전사가 메뚜기 식량창고를 약탈하기 위한 최대 식량을 구하는 문제이다. 예를 들어, 식량 창고가 `{1, 3, 1, 5}`
일때, 최대 약탈할 수 있는 식량은 `8`이다. 
- 이때, 식량창고를 약탈하기 위해 최소 한칸 이상 떨어진 식량 창고를 약탈해야 한다. `3 <= N <= 100`
- 첫째 줄에는 식량 창고 개수 `N`, 둘째 줄에는 식량 갯수가 주어진다. `0 <= K <= 1,000`
### 입력
```
4
1 3 1 5
```

### 출력
```
8
```

## 문제 풀이

먼저 문제의 점화식부터 세워보자.
만약 왼쪽부터 i를 털었을 때, i-1는 털지 못한다. 
- i - 1 번째를 털 경우, i는 털 수 없다.
- i - 2 번째를 털 경우, i는 털 수 있다.

최적의 해를 구한다고 가정했을 떄, 이 두가지만 생각하고 풀면 된다.
  
$a_i = max(a_{i-1}, a_{i-2} + k_i)$


<img width="546" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/395080e0-3dc4-4e6d-8cbc-a43117fe38d7">


```python
n  = int(input())

array = list(map(int, input().split())) # 모든 식량 정보

memo = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
memo[0] = array[0]
memo[1] = max(array[0], array[1])
for i in range(2, n):
    memo[i] = max(memo[i - 1], memo[i - 2] + array[i])

print(memo[n - 1])
```


---

# [실전3] 바닥 공사

|[🔗](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation.md#메모리-제약-사항)|시간 제한|메모리 제한|
|---|---|---|
|20분|1초|128MB|

<img width="444" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/749031f5-ccd6-445d-b73f-2175512a19ab">


가로가 `N`이고 세로가 2인 직사각형 바닥이 있을 때, 이 바닥을`1 X 2`, `2 X 1`, `2 X 2` 덮개로 채우고자 한다.

이때 바닥을 채우는 모든 경우의 수를 작성하세요.
예를 들어  2x`3`의 바닥을 채우는 경우의 수는 `5`이다.

- N : 1 <= N <= 1,000
- 2 X N 크기의 바닥을 채우는 방법 수는 `796,796`을 나눈 나머지를 출력한다. (결과값이 커짐을 방지하기 위함)

### 입력
```
3
```

### 출력
```
8
```

## 문제 풀이
이 문제도 위 처럼 `i-3` 번째 이하의 위치에 대해 생각할 필요 없다. 최대 2x2 형태의 직사각형이기 때문에 채울 수 있는 직사각형 크기는 두가지의 경우이다.

- i - 1 까지 채워져 있을 경우 : 2 X 1
- i - 2 까지 채워져 있을 경우 : 2 X 2, 2 X 1(2개)이다. 

<img width="658" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/1380584f-e565-47cf-8377-11c21459b9ae">

```python

n = int(input())
memo = [0] * 1001

for i in range(3, n+1):
    memo[0] = 1
    memo[1] = 3
    memo[i] = max(memo[i - 1], memo[i - 2] * 2)

print(memo[i])

```
<img width="1084" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/4e154d37-916e-4378-a450-3dc3d77514d3">

# [실전4] 효율적인 화폐 구성

|[🔗](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation.md#메모리-제약-사항)|시간 제한|메모리 제한|
|---|---|---|
|30분|1초|128MB|

N 가지 종류의 화폐가 있을 때, 이 화폐들을 최소한으로 이용해 합이 M원이 되도록 한다. 사용한 화폐의 구성은 같지만 순서만 다른 경우 같은 경우로 구분한다.

- 첫째 줄에 `N`과 `M`이 주어진다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000)
- 이후 N개의 줄에는 각 화폐의 가치가 주어진다. (가치 ≤ 10,000)
- 출력할 때는, M원을 만들기 위한 **최소 화폐 개수**를 출력하며 불가능한 경우 **-1**을 반환한다.




### 입력
```
2 15
2
3
```


```
3 4
3
5
7
```

### 출력

```
5
```
```
-1
```


## 문제 풀이

이번 문제는 이전에 풀었던 거스름돈 문제와 유사하나 큰단위가 작은단위의 배수가 아니기 때문에 해결할 수 없고 다이나믹 프로그래밍으로 풀어야 한다.

즉, 적은 금액부터 큰 금액까지 확인하면서 차례대로 만들 수 있는 최소 한의 화폐 갯수를 찾아야 한다.

- 금액 $i$를 만들 수 있는 최소한의 화폐 개수를 $a_i$
- 화폐의 단위 $k$
- 금액 $i-k$를 만들 수 있는 최소환의 화폐 개수는 $a_{i-k}$

그렇다면 점화식을 아래와 같이 작성할 수 있다.
- $a_{i-k}$를 만드는 방법이 존재하는 경우 $a_i = min(a_i, a_{i-k}+1)$
- $a_{i-k}$를 만드는 방법이 존재하지 않는 경우 $a_i = 10,001$

만약, 예를 들어 입력이 아래와 같을 경우,
```
3 7
2
3
5
```
<img width="720" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/33f7d481-aa81-4b5e-b2fa-4a4bf2ccc368">

위처럼 계산하면 된다.

```python
# 정수 n과 m을 입력받는다.
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력 받는다.
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
memo = [10001] * (m + 1) # 0~15개의 초기 리스트 값을 구성합니다.

# 다이나믹 프로그래밍 진행 (Bottom Up)
memo[0] = 0 # 동전이 없으면 무조건 0

for i in range(n):
    for j in range(array[i], m + 1): # 2 ~ 15 # 3 ~ 15
        if memo[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            memo[j] = min(memo[j], memo[j - array[i]] + 1)

# 계산된 결과
if memo[m] == 10001: # 만약 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(memo[m]) # 15일 때 사용할 수 있는 최소 개수


```