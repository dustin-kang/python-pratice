# 1

n , m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if  m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
## 제가 작성했었던 코드가 비슷헀습니다.

# 2 Best

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