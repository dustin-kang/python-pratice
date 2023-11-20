"""
그리디 - 큰수의 법칙
5 8 3
2 4 5 4 6

문제는 다음과 같이 풀었는데 결국 중요한 건 반복되는 수열을 파악하는 것이다. 

"""

n, m, k =  map(int, input().split())
data = list(map(int, input().split()))

result = 0
count = 0
data.sort(reverse=True) # 큰 수부터 합을 할 수  있도록 값을 더합니다.

while m > 0:
    result += data[0]
    m -= 1
    count += 1
    if count == k:
        result += data[1]
        m -=1
        count = 0


# m이 총 횟수라 할 때, 인덱스를 3번 반복할 수 있으니까 결론적으로 총 4번의 수가 더해지면 원점으로 돌아가 다시 반복
# 6 6 6 5 +  6 6 6 5 = 46
# m / 4 * k + m % 4 (나누어지지 않는 경우를 대비해 m %4 를 더한다.)


first = data[0]
second = data[1]

count = (m / k + 1) * k
count = m % k

result += count * first
result += (m-count) * second

# 여기서 중요한 건 m의 반복수가 100억 이상인 경우 반복문을 사용할 수 없게 된다.