"""
그리디 - 만들 수 없는 금액
"""
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin: # Target을 만들 수 없는 경우
        break
    target += coin # 만들 수 있으면 업데이트

print(target)