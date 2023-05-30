# 소수의 판별 2 (에라토스테네스의 체)

> 📌 **소수(Prime number)** : 2보다 큰 자연 수 중 1과 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수를 말합니다.
> 1. 2보다 커야 한다.
> 2. 1과 자신을 제외하고 나누어 떨어지지 않는다. 즉, _`n % 2 != 0`_

우리는 이전에 X라는 수가 소수인지 아닌지 효율적으로 판별하는 알고리즘을 구현하였습니다.[🔗링크](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/math-algorithm/judge_prime_number.md) 

만약에 이 X라는 수가 하나가 아니라 **여러개라면 어떻게 할까요?**  **`에라토스테네스의 체`** 알고리즘은 **N보다 작거나 같은 모든 소수를 찾을 때 사용하는 알고리즘**입니다. 

1. `2`부터 `N`까지의 모든 자연수를 나열합니다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 `i`를 찾습니다.
3. 남은 수 중에서 `i`의 배수를 모두 제거합니다. (단, `i`는 제거하지 않습니다.)
4. 더 이상 반복할 수 없을 때까지 2번과 3번을 반복합니다.

글로 설명하기엔 너무 어려울 것이니 아래 그림을 보고 알고리즘을 이해하실 수 있으실 것입니다. 

<img width="618" alt="image" src="https://user-images.githubusercontent.com/55238671/226808101-6abcbff1-a23b-45a4-a88b-123fc56d335a.png">

> 📌 매 반복마다 처리하지 않은 작은 수를 찾게 되는데 이때도 **N의 제곱근까지만 증가시켜 확인**하면 됩니다.
> 
> 📌 가끔 1이 소수인지 물어보기도 하는데 **1인 소수가 아니므로 `False`** 처리 하면 됩니다.

```python
import math

n = 1000 # to judge from 2 to 1000
array = [True for i in range(n+1)] # At first, All of number is prime number(True)

# Algorithm
for i in range(2, math.sqrt(n) + 1): # 0[0], 1[1] is not prime 
    if array[i] == True: # if i is prime
        j = 2 # Delete All of multiple except for i 
        while i * j <= n: # i * j, i * (j+1), i* (j+2)..
            array[i * j] = False
            j += 1
        
# print all of prime
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')

```

에라토스테네스의 체 알고리즘은 선형시간 정도와 비슷할 정도로 **빠른 알고리즘**입니다.
다만 **메모리가 많이 필요한** 알고리즘 입니다. 1000개의 범위는 그럴싸할지 몰라도 100000 아니.. 1,000,000 되면 메모리가 장난 아니겠죠. 
 $$O(N\log\log N) \\ N = 1000, \log\log N = 4 $$


 #### [👨‍💻 관련 문제 확인하기 소수 구하기](https://github.com/dustin-kang/Programming-Team-Notes/issues/6)
- [간단하게 구한 에라토스테네스의 체](https://github.com/dustin-kang/Programming-Team-Notes/issues/6#issuecomment-1484809963)
