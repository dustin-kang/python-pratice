# sorting\_pratice

> **INDEX**
>
> * [실전 문제 : 위에서 아래로](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/sorting/sorting\_pratice.md#%EC%8B%A4%EC%A0%841-%EC%9C%84%EC%97%90%EC%84%9C-%EC%95%84%EB%9E%98%EB%A1%9C)
> * [실전 문제 : 성적이 낮은 순서로 학생 출력하기](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/sorting/sorting\_pratice.md#%EC%8B%A4%EC%A0%842-%EC%84%B1%EC%A0%81%EC%9D%B4-%EB%82%AE%EC%9D%80-%EC%88%9C%EC%84%9C%EB%A1%9C-%ED%95%99%EC%83%9D-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0)
> * [실전 문제 : 두 배열의 원소 교체](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/sorting/sorting\_pratice.md#%EC%8B%A4%EC%A0%843-%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%9B%90%EC%86%8C-%EA%B5%90%EC%B2%B4)

## \[실전1] 위에서 아래로

| [🔗](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/implementation/implementation.md#%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%A0%9C%EC%95%BD-%EC%82%AC%ED%95%AD) | 시간 제한 | 메모리 제한 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------ |
| 15분                                                                                                                                                                        | 1초    | 128MB  |

첫째줄에 수열에 속해 있는 수의 개수 N이 주어지고 다음 줄부터 N개의 수가 입력된다. 수열을 내림차순으로 정렬하는 프로그램을 만들어라

#### 입력

```
3
15
27
12
```

#### 출력

```
27
15
12
```

**코드**

```python

n = int(input())

answer = []
for _ in range(n):
    answer.append(int(input()))

answer.sort(reverse=True)

for i in range(n):
    print(answer[i], end=' ')
```

***

## \[실전2] 성적이 낮은 순서로 학생 출력하기

| [🔗](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/implementation/implementation.md#%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%A0%9C%EC%95%BD-%EC%82%AC%ED%95%AD) | 시간 제한 | 메모리 제한 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------ |
| 20분                                                                                                                                                                        | 1초    | 128MB  |

N명의 학생 정보가 있다. 학생 정보는 이름과 성적으로 구분되는데 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하시오.

#### 입력

```
2
홍길동 95
이순신 77
```

#### 출력

```
이순신 홍길동
```

### 문제 풀이

```python
n = int(input())

array = []

for _ in range(n):
    name, score = map(str, input().split())
    array.append((name, int(score)))

array = sorted(array, key = lambda x: x[1]) 

for i in array:
    print(i[0], end=' ')
```

***

## \[실전3] 두 배열의 원소 교체

| [🔗](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/implementation/implementation.md#%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%A0%9C%EC%95%BD-%EC%82%AC%ED%95%AD) | 시간 제한 | 메모리 제한 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------ |
| 20분                                                                                                                                                                        | 2초    | 128MB  |

배열 A의 모든 원소의 합이 최대값이 되기 위해 배열 A와 배열 B를 바꿔치기 할 수 있다. 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

* N : 배열의 길이
* K : 바꿔치기 연산 횟수
* 첫째 줄에는 N, K가 주어지며 다음 줄에는 배열 A와 배열 B의 값들이 주어집니다.

#### 입력

```
5 3
1 2 5 4 3
5 5 6 6 5
```

#### 출력

```
26
```

#### 문제 해설

* 우선, 배열 A를 오름차순, 배열 B를 내림차순으로 정렬한다.
* 서로 값들을 비교해가면서 변경한다.

**코드**

```python
n, k = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)


index = 0
for i in range(n):
    if k > 0 and arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
        k -= 1

"""
for i in range(n):
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break
"""

print(sum(arrA))
```
