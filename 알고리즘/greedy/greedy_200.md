
## [실전1] 큰수의 법칙

> 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙이라고 합니다.

만약 2,4,5,4,6으로 이루어진 배열이 있으며 M이 8이고 K가 3이라고 할 때 큰 수의 법칙에 따른 결과를 출력하라.

`6 + 6 + 6 + 5 + 6 + 6 + 6 + 5`인 `46`이 됩니다.

* 배열의 크기 N
* 숫자가 더해지는 횟수 M
* 최대 연속해서 더할 수 있는 횟수 K

#### 입력

```
5 8 3
2 4 5 4 6
```

#### 출력

```
46
```

### 문제 풀이

```python
n, m, k = map(int, input().split(" "))
array = list(map(int, input().split(" ")))

array.sort() # 입력 받은 수 정렬하기
count = 0
answer = 0

while m > 0: # 숫자 횟수가 m번 다채워지면 종료
    if count == k: # 최대 연속 덧셈 횟수를 채운 경우
        count = 0
        m -= 1 # 더할 때 마다 1씩 빼기
        answer += array[-2] # 두번째 큰 수 더하기
        print(f'+ {array[-2]}', end ='')
    else : # 그렇지 않은 경우 
        m -= 1
        count += 1
        answer += array[-1] # 첫번째 큰 수 더하기
        print(f'+ {array[-1]}', end ='')
print()
print(answer)
```

#### 반복되는 수열 찾기

이 문제에서는 `6 6 6 5` 로 덧셈이 반복되는 걸 알 수 있습니다.

![image](https://user-images.githubusercontent.com/55238671/234258369-c8161ffc-8303-495c-ab79-319185d5864b.png)

```python
n , m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 구하기
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기
print(result)
```

***

## [실전2] 숫자 카드 게임

> 여러가지 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임입니다.

룰은 아래와 같습니다.

1. 카드들의 형태가 N \* M 형태로 놓여있다.
2. 먼저 뽑고자 할 카드가 포함되어 있는 행을 선택한다.
3. 그다음, 가장 숫자가 낮은 카드를 뽑는다.
4. 따라서, 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자 카드를 뽑을 수 있게 전략을 세워라.

* 행의 갯수 N과 열의 갯수 M이 공백을 기준으로 자연수로 주어집니다. (1 <= N, M <= 100>)
* 둘째 줄 부터 N개의 줄을 걸쳐 각 카드에 적힌 숫자가 주어집니다. (1 이상 10,000 이하)

#### 입력

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

#### 출력

```
2
```

```
3
```

### 문제 풀이

```python
m, n = map(int, input().split())
answer = []
for i in range(m):
    row = list(map(int, input().split()))
    answer.append(min(row))

print(max(answer))
```

***

## \[실전3] 1이 될 때까지

어떠한 수 N이 1이 될때까지 두 과정 중 하나를 반복 수행한다. 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예를 들어 N이 17이고 K가 4일 경우, 1번 과정을 수행하면 16이 되고 2번을 수행하면 N은 1이 된다.

#### 입력

```
25 5
```

#### 출력

```
2
```

### 문제 풀이

```python
n, k = map(int, input().split())
count = 0
while n > 1:
    if n % k != 0: # n이랑 k가 나누어 떨어지지 않을 때
        n -= 1
        count += 1
    else : # n이랑 k가 나누어 떨어질 때
        n = n // k
        count += 1

print(count)

```

```python
n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
```

## with
[무지의 먹방 라이브 - 2019 카카오 신입 공채](https://school.programmers.co.kr/learn/courses/30/lessons/42891)