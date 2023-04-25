# [실전1] 큰수의 법칙

> 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙이라고 합니다.

만약 2,4,5,4,6으로 이루어진 배열이 있으며 M이 8이고 K가 3이라고 할 때 큰 수의 법칙에 따른 결과를 출력하라.

`6 + 6 + 6 + 5 + 6 + 6 + 6 + 5`인 `46`이 됩니다.

- 배열의 크기 N
- 숫자가 더해지는 횟수 M
- 최대 연속해서 더할 수 있는 횟수 K

### 입력
```
5 8 3
2 4 5 4 6
```
### 출력
```
46
```

## 문제 풀이
```python
n, m, k = map(int, input().split(" "))
array = list(map(int, input().split(" ")))

array.sort() # 입력 받은 수 정렬하기
count = 0
answer = 0

while m > 0: # 숫자 횟수가 m번 다채워지면 종료
    if count == k: # 최대 연속 덧셈 횟수를 채운 경우
        count = 0
        m -= 1 # 더할 때 마다 1씩 빼기
        answer += array[-2] # 두번째 큰 수 더하기
        print(f'+ {array[-2]}', end ='')
    else : # 그렇지 않은 경우 
        m -= 1
        count += 1
        answer += array[-1] # 첫번째 큰 수 더하기
        print(f'+ {array[-1]}', end ='')
print()
print(answer)
```

## [📔answer](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/greedy/p_big_number.py)

### 반복되는 수열 찾기
이 문제에서는 `6 6 6 5` 로 덧셈이 반복되는 걸 알 수 있습니다. 

<img width="495" alt="image" src="https://user-images.githubusercontent.com/55238671/234258369-c8161ffc-8303-495c-ab79-319185d5864b.png">

```python
n , m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 구하기
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기
print(result)
```

