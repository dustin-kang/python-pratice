"""
다이나믹 프로그래밍 - 개미 전사

4
1 3 1 5
"""

n = int(input()) # 창고의 갯수 4
vault = list(map(int, input().split())) # [1,3,1,5]

# 우리가 찾아야할 것은... 최대 먹이 값! 
# but, 1칸 이상으로 떨어져야함.
# 1 -> 1, 3 -> 5 == 8개가 최대 갯수

dp_table = [0] * 100 # 최대 창고의 수는 100개

dp_table[0] = vault[0] # 1
dp_table[1] = vault[1] # 3

for i in range(2, n):
    dp_table[i] = max(dp_table[i-1], dp_table[i-2] + vault[i]) 
    # 이전 값과 현재 값 + 전전 값 중 큰 값을 저장(1+1, 3)
    # (3 + 5, 3) = 8

print(dp_table[n-1])