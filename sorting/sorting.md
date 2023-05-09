# 정렬 알고리즘
> 특정한 기준에 따라 순서대로 나열하는 알고리즘

정렬을 구현하기 위해 파이썬에서는 `.sort()` 나 `sorted()` 라이브리러를 이용해 쉽게 정렬을 구현할 수 있다. 시간 복잡도도 $O(NlogN)$으로 간단히 수행할 수 있다.

### 선택 정렬
> 가장 작은 것을 **선택**한다는 의미로 선택 정렬 알고리즘이라고 합니다.

- 위 그림처럼 선택 정렬은 N-1번 반복하면 정렬이 됩니다.
- 시간 복잡도는 점점 $N$부터 데이터를 감소하면서 실행했으므로 $O(N^2)$로 표기합니다.
  


```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)
```

> #### 📌 swap
> 특정 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업을 말합니다. `array[0], array[1] = array[1], array[0]`


### 삽입 정렬
> 특정 데이터를 적절한 위치에 **삽입**하는 알고리즘으로 위치에 들어가기 전까지는 이미 정렬된 상태라고 가정합니다.

- 필요할 때만 위치를 바꾸므로 데이터가 **거의 정렬되어 있을 때만 효율적인** 알고리즘입니다.

- 최악의 경우는 $O(N^2)$이지만 최선의 경우, 앞에 정렬이 된 상태라면 $O(N)$입니다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # start부터 end까지 1씩 감소
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
```

### 버블 정렬
> 인접한 두 데이터를 비교해서 자리를 바꾸는 정렬 알고리즘입니다.

- 시간 복잡도는 $O(N^2)$ 입니다. 삽입정렬과 똑같이 완전히 정렬된 경우는 O(N)입니다.

```python
for i in range(len(array)):
    for j in range(len(array) - i):
        if array[j] > array[j+1]:
            array[j] , array[j+1] = array[j+1] > array[j]
```

|  | 선택 정렬 | 삽입 정렬 | 버블 정렬 |
| --- | --- | --- | --- |
| 정의 | 최소값과 가장 앞데이터 교환 | 처리가 안되어있는 데이터 부터 차례대로 정렬 | 서로 이웃한 두원소의 크기를 비교하여 교환 반복 |
| 특징 | 이웃하지 않은 노드와 교환하므로 불안정 | 실행 시간 측면에서 난이도 비해 효율적 (소량에 적절) | 간단하면서 비효율적, 하지만 이웃노드와 교환으로 안정적 |
| 시간복잡도 | $O(N^2)$ | $O(N^2)$ (최선 $O(N)$) | $O(N^2)$ |


## 퀵 정렬
> **피벗(pivot)** 으로 기준점으로 정해 피벗 보다 크면 오른쪽, 작으면 왼쪽으로 이동하고 재귀 용법을 활용해 함수를 반복시켜 정렬하는 알고리즘

- 피벗을 설정해 리스트를 분할하는 방식에는 여러 방식이 있는데 그 중 [호어 분할 방식]()을 기준으로 많이 사용된다.
- 평균적으로 시간 복잡도는 $O(NlogN)$이지만 최악의 경우 $O(N^2)$이다. 이유는 **점점 분할을 할 수록 절반으로 감소되기 때문에 분할 횟수도 기하급수적으로 감소하기 때문**입니다.
- pivot이 가장 크거나 가장 작은 경우에는 모든 데이터를 비교해야합니다.
- 위 예제 처럼 데이터가 이미 정렬되어 있거나 가장 왼쪽을 pivot으로 두면 느립니다.
- [직관적인 퀵 정렬 알고리즘]()

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우
        return
    pivot = start # pivot
    left = start +1
    right = end

    while left <= right:
        # 피벗보다 크거나 같은 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작거나 같은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right += 1
        
        if left > right:
            # 엇갈렸다면 피벗과 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았다면 작은 데이터와 교체
            array[right], array[left] = array[left], array[right]
    
    # 각각 오른쪽 왼쪽으로 나누어 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
```
## 병합 정렬


## 계수 정렬
> 특정 조건이 부합할 때만 사용하는 매우 빠른 알고리즘

- 데이터 크기가 제한 되어 정수 형태를 표현할 때만 사용하는 알고리즘입니다.

- 가장 작은 데이터와 큰 데이터의 차이가 1,000,000을 넘지 않아야합니다.

- 계수 정렬의 시간 복잡도는 $O(N+K)$ 입니다.

- 현존하는 정렬 알고리즘 중에 기수 정렬과 더불어 가장 빠른 알고리즘입니다. 

```python
array = [7,5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+ 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')
```


- [실전 문제 : 위에서 아래로](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/sorting/sorting_pratice.md#실전1-위에서-아래로)
- [실전 문제 : 성적이 낮은 순서로 학생 출력하기](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/sorting/sorting_pratice.md#실전2-성적이-낮은-순서로-학생-출력하기)
- [실전 문제 : 두 배열의 원소 교체](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/sorting/sorting_pratice.md#실전3-두-배열의-원소-교체)
