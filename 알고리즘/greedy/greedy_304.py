"""
만들 수 없는 금액

<문제 해석>
N개의 동전을 이용해 만들 수 없는 금액 중 최소값 반환

<입력>
5
3 2 1 1 9

<출력>
8
"""


# 문제풀이
n = int(input())
answer = 1
lst = set()
coins = list(map(int, input().split()))
for i in range(n):
    for j in range(1,n+1):
        lst.add(sum(coins[i:j]))

while True:
    if answer not in lst:
        print(answer)
        break
    else:
        answer += 1

# 정답

coins.sort()

target = 1 # 처음 금액을 만들 수 있는지 확인
for x in coins: 
    if target < x:
        break
    target += x # 1 + 1 = 2의 경우, 1까지의 모든 금액을 만들 수 있다는 의미

print(target)