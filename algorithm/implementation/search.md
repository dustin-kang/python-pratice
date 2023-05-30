# 탐색
## 순차 탐색(Sequential Search)
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서 부터 하나씩 차례대로 확인하는 방법

- 시간 복잡도는 $O(N)$입니다.
- 특정한 값을 가지는 원소의 개수를 셀 때 `count()`같은 메소드를 이용해 탐색을 합니다.

## 이진 탐색(Binary Search)
찾으려는 데이터와 중간점에 있는 데이터를 반복적으로 비교하며 원하는 데이터를 찾는 방법

<img width="520" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/658f4a8f-6728-481c-84c5-ea4344aae449">


- **반드시 이미 정렬**되어 있어야한 사용할 수 있습니다.
- 인덱스를 통해 중간점을 구할때 **소수점은 버립니다.**
- 퀵 정렬과 비슷하게 절반씩 데이터가 줄어들기 때문에 $O(logN)$입니다.

### 재귀함수로 이진 탐색 구현하기
```python
def binary_search(array, target, start, end):
    # 정렬이 되어있지 않은 경우
    if start > end:
        return None 
    
    mid = (start + end) // 2 # 중간점 반환
    
    # 찾고자 하는 데이터가 중간값, 중간 초과, 중간 미만 일 경우
    if array[mid] == target: 
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

result = binary_search(array, target, 0, 9):
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

- [👉 반복문으로 구현한 이진탐색](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/search_pratice.py)

> 📌 이진 탐색 알고리즘은 다른 알고리즘과 같이 혼합해서 출제되니 코드를 잘 암기하고 있어야 한다.

예로, 데이터의 개수가 1,000만개를 넘어 1,000억 이상이라면 이진 탐색을 사용해야 한다. 이럴 때 `input()` 함수를 사용하는 것보다 `readline()` 함수를 사용하면 시간 초과를 피할 수 있다.

```python
import sys
input_data = sys.stdin.readline.rstrip()

print(input_data)
```
`readline()`을 입력하면 엔터가 줄바꿈 기호로 입력되는데 공백을 제거하기 위해 `rstrip()`을 사용한다.


---
- [실전 문제 : 부품 찾기]()
- [실전 문제 : 떡볶이 떡 만들기]()



