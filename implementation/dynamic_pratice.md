> **INDEX**
> - [실전 문제 : 1로 만들기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/sorting/dynamic_pratice.md#실전1-1로-만들기)
> - [실전 문제 : 개미 전사](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/sorting/dynamic_pratice.md#실전2-개미-전사)
> - [실전 문제 : 바닥공사](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/sorting/dynamic_pratice.md#실전3-바닥공사)
> - [실전 문제 : 효율적인 화폐 구성](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/sorting/dynamic_pratice.md#실전4-효율적인-화폐-구성)


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

```

## 문제 풀이

우선 가장 긴 떡의 중간 값을 구한다음 합이 6과 같을 때까지 반복한다.고 생각해봤다.


```python

```
