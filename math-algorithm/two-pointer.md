# 투 포인터
투포인터(Two Pointers) 알고리즘은 리스트를 순차적으로 접근해야할 때 **점(Pointer)를 두개로 두어 위치를 기록**하는 알고리즘입니다.

> 예를 들어서, 한 반에 30명중 1번~ 10번의 학생 번호를  부를 때, 1번 부터 10번까지 하나하나 부를 수 있지만 1번부터 10번까지의 학생이라고 칭할 수 있습니다. 이와 같이, 시작점과 끝점을 두어 범위를 표현할 수 있습니다.

그럼 대표적으로 어떤 유형으로 투 포인터 알고리즘을 사용할 수 있는지 알아봅시다. 

## 💡 **특정 합**을 가지는 **연속** 수열 찾기
여기서 중요한 건 **특정합**과 **연속**되는 리스트입니다. 물론 정수로 된 리스트여야하고 음수가 들어있으면 안됩니다.(그 이유는 차차 알게될 것입니다.)

만약 우리가 `1,2,3,2,5`를 차례대로 원소를 갖는 리스트가 주어졌을 때 합이 `5`가 되는 부분 연속 수열을 어떻게 찾을 수 있을까요?

물론 답은 `2+3, 3+2, 5` 입니다. 투포인터 알고리즘으로 풀어보면 부분 연속 수열을 찾을 수 있습니다.
1. 시작점과 끝점이 `첫 번째 원소의 인덱스(0)`을 가리킵니다.
2. 현재 부분합이 `M`과 같다면 카운트 한다. (아! 여기서 `M`은 특정합입니당,,)
   1. 만약 `M`보다 작으면 `end`을 `1` 증가시킵니다.
   2. 만약 `M`보다 크면 `start`를 `1` 증가시킵니다.
3. 모든 경우를 확인할 때까지 반복합니다.

> 📌 이문제를 투 포인터 알고리즘으로 해결할 수 있는 이유는 시작점을 오른쪽으로 이동시키면 합이 감소하고 끝점을 오른쪽으로 이동시키면 합이 증가하기 떄문입니다. 

<img width="591" alt="image" src="https://user-images.githubusercontent.com/55238671/227105176-52d7dfe3-583b-4409-ae9e-daf89bdcab94.png">

```python
n = 5 # number of data
m = 5 # subsum
data = [1, 2, 3, 2, 5] # Array

count = 0
interval_sum = 0 # current subsum
end = 0

# start ++
for start in range(n):
    # end condition
    while interval_sum < m  and end < n :
        interval_sum += data[end]
        end += 1
    # current subsum == m -> +count
    if interval_sum == m:
        count += 1
    interval_sum -= data[start] # start condition

print(count)
```

## 💡 두 리스트를 합해서 하나의 리스트로 정렬하기
이  문제는 우선 **정렬이 된** 2개의 리스트가 주어집니다. 이 두개의 리스트를 **합쳐 정렬된 결과를 계산**하는 것입니다. 

1. 정렬된 리스트 `A, B`를 입력받고 각 리스트마다 가장 작은 원소를 `i,j`가 가리키도록 합니다.
2. `A[i]` 와 `B[j]` 중 비교를 통해 더 작은 원소를 결과 리스트에 담습니다. 
3. 리스트 `A`와 `B`가 처리할 원소가 없을 때 까지 반.복^^

<img width="665" alt="image" src="https://user-images.githubusercontent.com/55238671/227105247-657e624d-818c-4c4a-a6f3-18c6b8fd78bd.png">

결과적으로, 각 리스트의 데이터 갯수가 N, M이라고 할 때 시간 복잡도는 $O(N+M)$ 입니다. 왜냐하면 단순하게 한번씩 순회하기 때문이죠.

> 📌 이미 정렬되어있는 리스트의 합집합은 **[병합정렬(Merge Sort)]()** 과 같은 알고리즘입니다.

```python
# lists
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n + m) # result list
i = 0 # pointers
j = 0
k = 0 


while i < n or j < m:
    # 리스트 B의 모든 원소가 이미 처리되었거나 리스트 B의 원소가 더 작은 경우
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    
    #리스트 A의 모든 원소가 이미 처리되었거나 리스트 B의 원소가 더 작은 경우
    else:
        result[k] = b[j]
        j += 1
    k += 1

# 결과 출력
for i in result:
    print(i, end='')
```
