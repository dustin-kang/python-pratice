# 순열과 조합

다양한 알고리즘 문제에서 **순열(Permutation)과 조합(Combination)** 을 찾는 과정을 요구합니다. 

물론 **재귀함수나 반복문** 을 이용하여 직접 구현할 수 있으나 Python에서는 **순열과 조합 기능을 제공** 하는 라이브러리가 있습니다.(Python 3 이상)

> 📌 **경우의 수**
> 
>경우의 수는 **한번의 시행에서 일어날 수 있는 사건의 가지 수**를 의미합니다. 주사위 던지기의 경우 경우의 수는  {1, 2, 3, 4, 5, 6} 중 하나인 셈이죠. (6가지)


<img width="609" alt="image" src="https://user-images.githubusercontent.com/55238671/227470957-e725af82-94f6-4e0f-885e-f55d67ef9cd8.png">


## 💡 순열(Permutation $nPr$)

서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것을 말합니다.

`itertools` 라이브러리에서 `permutations` 함수를 통해 손쉽게 구현할 수 있습니다.

```python
import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))

# [1, 2] [2, 1]
```

$$
nPr = n! / (n-r)!
$$

## 💡 조합(Combination $nCr$)

서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것을 말합니다.

`itertools` 라이브러리에서 `combinations` 함수를 통해 손쉽게 구현할 수 있습니다.

```python
import itertools

data = [1, 2, 3]

for x in itertools.permutations(data, 2):
    print(list(x), end=' ')

# [1, 2] [1, 3] [2, 3]
```

### [👨‍💻 파이썬 기본 문법에서 확인하기](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/Pythoncode.ipynb)
