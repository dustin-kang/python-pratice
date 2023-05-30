# Recursive Function

<img width="462" alt="image" src="https://user-images.githubusercontent.com/55238671/235831800-a1c3d503-575a-4fa7-8e61-23eebb8e589a.png">


재귀함수는 자기 자신을 호출하는 함수를 의미합니다. [시에르핀스키의 삼각형](https://en.wikipedia.org/wiki/Sierpiński_triangle)이나 프랙탈 구조를 생각해보면 된다.

재귀함수를 사용하다보면 아래 에러와 마주칠 수 있다. 아래 에러는 재귀의 최대 깊이를 초과(exceed)했다고 나오는 오류 이다.
```
Recursive Error : maximum recursive depth exceeded while picking an object
```

## 재귀함수 구현
그렇다면 실제로 재귀 함수를 구현해보자. 재귀함수를 구현할 때 반드시 필요한 몇가지가 있다.

> 1. 종료 조건을 명시해야 한다.
> 2. 마지막에 호출한 함수가 먼저 종료된다. (스택 구조)
> 3. 점화식을 사용한다. (1 = n = 0 or 1 , n * n-1 = n > 1)

```python
def factorial(n):
    if n <= 1: # 종료 조건
        return 1
    return n * fact(n - 1) # n * (n-1)!

print(factorial(5))
```

## 재귀함수 이점
반복문(iterative)을 사용했을 때와 재귀함수(recursive)를 사용했을 때를 비교해보면, **재귀함수가 더 간결해진다**라는 것을 알 수 있다.

이유는 소스코드에 수학의 점화식(재귀식)을 그대로 옮겼기 때문이다. 
