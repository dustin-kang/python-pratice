"""
다이나믹 프로그래밍

못생긴 수 : 2,3,5를 소인수로 가지는 수(2,3,5를 약수로 가지는 합성 수)
이때 n번째 못생긴 수를 찾는 프로그램을 작성하시오.

1 <= n <= 1000


10 -> 12
4 -> 4
"""

n = int(input())

ugly = [0] * n
ugly[0] = 1

"""
여기서 중요한 건 2,3,5를 소인수로 가지기 떄문에
못생긴 수에 2,3,5를 곱한 수 또한 못생긴 수에 포함한다.
"""

i2, i3, i5 = 0, 0, 0 # 인덱스
next2, next3, next5 = 2,3,5

for l in range(1, n): # 1부터 n까지 차례대로
    ugly[l] = min(next2, next3, next5) 
    if ugly[l] == next2: 
        i2 += 1
        next2 = ugly[i2] * 2 # 다음수는 i2의 수의 배수
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1]) # n번째 못생긴 수 출력





