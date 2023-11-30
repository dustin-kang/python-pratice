"""
그리디 - 1이 될때 까지

25 5

2
"""

n , k = map(int,input().split())
count = 0

# 1번. n에서 1을 뺀다
# 2번. n에서 k로 나눈다.

# 일반 방법
while n > 1:
    if n % k == 0:
        n = n // k
    else:
        n -= 1
    count += 1


# 최적화된 방법
# 나눌때 한번에 빼는 방식
while True:
    target = (n // k) * 3 # 나누기가 가능할 숫자(1번의 n값)
    count += (n - target) # 빼야 되는 횟수(2번)
    n = target # n = 24

    # 더이상 나누기가 안되는 경우
    if n < k:
        break # n = 0 종료

    # 나누기!
    n //= k 
    count += 1 

count += (n - 1) # 6
print(count)