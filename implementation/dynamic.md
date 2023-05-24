# Dynamic Programming(동적 계획법)

- 메모리 공간을 더 사용하여 연산 속도를 증가시킬 수 있다.
- 큰문제를 작은 문제로 나누어 구한 정답이 큰 문제와 동일할 경우 풀 수 있다.
- 시간 복잡도는 $O(N)$이다. 왜냐하면 한 번 구한 결과는 다시 구하지 않기 때문이다.

다이나믹 프로그래밍의 방식에는 두가지 방식으로 나뉜다.
#### 탑다운 방식(Top-down, Memoization)
- 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
- 재귀 함수를 이용한다.
#### 보텀업 방식(bottom-up)
- 작은 문제부터 차근차근 답을 도출하는 방식
- 반복문을 이용한다.

> 📌 우리가 흔하게 접했던 동적 할당(Dynamic Allocation)은 실행 중 프로그램 실행에 필요한 메모리를 할당하는 기법이다. 하지만 여기서 **`다이나믹`이 동적 계획법의 `다이나믹`과는 다른 의미으로 유의해두자.**

## Memoization (메모이제이션)
다이나믹 프로그랭을 구현하는 방법 중 한 종류로, **한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 가져오는 기법이다.**

```python
memo = [0] * 100 # 메모이제이션을 하기 위해 리스트 초기화

## Top-Down
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if  memo[x] ! == 0: # 만약 계산한 적이 있는 경우
        return d[x]
    
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]


print(fibo(99))

## Bottom-up
memo[1] = 1
memo[2] = 2
n = 99

for i in range(3, n+1):
    memo[i] = memo[i - 1] + memo[i - 2]
```

위 코드 처럼 큰문제를 작은 문제로 나누고 같은 문제라면 한번씩만 풀어 효율적으로 해결하는 알고리즘이다.

사실 퀵 정렬을 통해 비슷한 경험을 느꼈을 것이다. 여기서 다이나믹 프로그래밍과 분할 정복 알고리즘의 차이는 다이나믹 프로그래밍은 문제들이 서로 영향을 미친다는 점이다.

- 다이나믹 프로그래밍 : 이미 해결된 문제에 대한 답을 저장하고 해결할 필요 없이 반환한다.
- 퀵 정렬 : 원소 자리가 변경해도 피벗 값을 다시 처리할 필요없다.

재귀 함수대신 반복문을 사용한 동적 계획법은 오버헤드를 줄일 수 있어 훨씬 성능이 좋다.


> 💡 특정 문제가 완전 탐색으로 접근해도 시간이 오래걸린다면 다이나믹 프로그래밍을 적용해보자
> 💡 재귀함수를 작성한 뒤 메모이제이션 기법을 적용해도 좋은 방법이다.
> 💡 가능하면 탑다운 보다는 보텀업을 구현하는것을 권장한다. 이유는 시스템상 재귀함수의 스택 크기가 한정되어 있기 때문이다.

---
> - [실전 문제 : 1로 만들기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전1-1로-만들기)
> - [실전 문제 : 개미 전사](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전2-개미-전사)
> - [실전 문제 : 바닥공사](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전3-바닥-공사)
> - [실전 문제 : 효율적인 화폐 구성](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/dynamic_pratice.md#실전4-효율적인-화폐-구성)