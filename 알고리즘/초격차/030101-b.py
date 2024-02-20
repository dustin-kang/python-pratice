"""
블랙잭
https://www.acmicpc.net/problem/2798

N장에 카드가 있을 때 3장의 카드 합이 M를 넘지 않은 한으로 뽑는다.
전체 경우의수 : n(n-1)(n-2)/ 3! => 1,000,000(20,000,000 이하) 완전 탐색으로 풀 수 있다. 

"""

n, m = map(int, input().split())
array = list(map(int, input().split()))


result = 0
length = len(array)

for i in range(n-3):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = array[i] + array[j] + array[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)




