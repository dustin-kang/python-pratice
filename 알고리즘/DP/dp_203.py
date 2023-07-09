'''
바닥 공사

-input-
3
-output-
8
'''


n = int(input())
memo = [0] * 1001

for i in range(3, n+1):
    memo[1] = 1 # 1m
    memo[2] = 3 # 2m
    memo[i] = (memo[i - 1] + 2 * memo[i - 2]) % 796796
    # 2를 곱한 이유는 i-2까지 덮개가 채워있는 경우에는 2가지 경우가 존재하기 때문입니다.

print(memo[i])