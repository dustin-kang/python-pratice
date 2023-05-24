> **INDEX**
> - [실전 문제 : 부품-찾기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/sorting/search_pratice.md#실전1-부품-찾기)
> - [실전 문제 : 떡볶이 떡 만들기](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/sorting/search_pratice.md#실전2-떡볶이-떡-만들기)


# [실전1] 부품 찾기

|[🔗](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation.md#메모리-제약-사항)|시간 제한|메모리 제한|
|---|---|---|
|30분|1초|128MB|

전자 매장에 N개의 부품이 있을 때, 손님이 문의한 부품 M개가 모두 있는지 확인하는 프로그램을 작성한다.

- 정수 N과 M은 1 <= N,M <= 1,000,000 이다.
- 첫째 줄 공백으로 n과 m을 구분하여 존재하면 yes 아니면 no를 출력한다.

### 입력
```
5
8 3 7 9 2
3
5 7 9
```
### 출력
```
no yes yes
```


#### 코드

```python
def bs(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid +1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort() # 탐색 전 정렬은 필수

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = bs(array, i, 0, n-1)

    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")    
```

[👉 계수 정렬 답안]()
[👉 집합 자료형 답안]()

---

# [실전2] 떡볶이 떡 만들기

|[🔗](https://github.com/dongwoodev/Programming-Team-Notes/blob/Python/implementation/implementation.md#메모리-제약-사항)|시간 제한|메모리 제한|
|---|---|---|
|40분|2초|128MB|

일정하지 않은 길이의 떡을 자를 때 절단기 높이(`H`)를 지정하여 
- 높이가 `H` 보다 긴 떡은 H 위의 부분이 자를 것이고
- 높이가 `H` 보다 작은 떡은 자르지 않을 것이다.

그렇다면, 손님이 요청한 총 길이가 `M`일 때, `M`만큼 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 작성하시오.

- 떡의 개수 N 은 1 <= N <= 1,000,000
- 떡의 길이 M 은 1 <= M <= 2,000,000
- 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이 총합은 항상 M이상이고 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.


<img width="592" alt="image" src="https://github.com/dongwoodev/Programming-Team-Notes/assets/55238671/9efe3126-7d68-4125-9860-4ef8be6ad12a">


### 입력
```
4 6
19 15 10 17
```

### 출력
```
15
```

## 문제 풀이

우선 가장 긴 떡의 중간 값을 구한다음 합이 6과 같을 때까지 반복한다.고 생각해봤다.
- 떡을 더 잘라야 하는 경우
  - mid를 왼쪽으로 점점 이동
- 떡을 덜 잘라야 하는 경우
  - mid를 오른쪽으로 점점 이동


```python
# 떡 개수와 요청한 떡 길이
n, m = list(map(int, input().split(' ')))
# 떡들의 개별 높이
array = list(map(int, input().split()))


start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0 
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    
    if total < m : # 떡의 양이 부족한 경우 더 자르기
        end = mid -1
    else: # 떡의 양이 충분한 경우  덜 자르기
        result = mid
        start = mid + 1

print(result)
```
