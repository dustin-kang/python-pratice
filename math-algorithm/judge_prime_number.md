# 소수의 판별 1

> 📌 **소수(Prime number)** : 2보다 큰 자연 수 중 1과 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수를 말합니다.
> 1. 2보다 커야 한다.
> 2. 1과 자신을 제외하고 나누어 떨어지지 않는다. 즉, _`n % 2 != 0`_

예를 들어서 X가 소수인지 아닌지를 판별해야할 때, 어떤 방식으로 이 문제를 해결할 수 있을까?

## 💡 2부터 X-1까지 모든 수를 나눠보는 방법
말그대로 X를 2부터 X-1까지 모조리 나눠보는 방법입니다.

```python
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False # not prime number
    return True 

print(is_prime_number(6)) # 1, 2, 3, 6
print(is_prime_number(7)) # 1, 7
```

물론, 위처럼 문제는 해결할 수 있지만 X가 10억이라고 가정한다면 이 알고리즘은 **굉장히 비효율적인 알고리즘**일 것입니다.

## 💡 자연수의 약수 특징을 활용한 방법

소수 판별 알고리즘을 보다 빨리 동작하기 위해 **자연수의 약수의 특징과 원리**를 잘 활용해야합니다.

[]()

위 그림, 16의 약수를 보게되면 양쪽이 4를 기준으로 서로 대칭이라는 것을 알 수 있어요. 그렇다면, 우리는 굳이 1~ 16까지 확인을 안해도(반만 나누어 떨어지는지 확인해도) 약수인지 확인이 가능하죠. 이렇게 작성하게 되면, **시간 복잡도도 반으로 줄일 수 있습니다.**

```python
import math

def is_prime_number(x):
    for i in range(2, math.sqrt(x)+1):
        if x % 2 == 0:
            return False
    return True

print(is_prime_number(6)) # 1, 2, 3, 6
print(is_prime_number(7)) # 1, 7
```


