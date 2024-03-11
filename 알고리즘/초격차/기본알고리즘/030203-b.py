"""
Z
중(40분)
재귀함수
https://www.acmicpc.net/problem/1074

2^N * 2^N(1<=N<=15), r열 C행(0<=r, c<2^N)을 몇번째로 방문했는지
"""

N, r, C = map(int, input().split())

# Z : 0,0을 기준으로 X, y의 숫자 (헷갈리지 말기,, row : x, column : y)
def Z(sz, x, y):
    if sz == 1:
        # 한칸일 때는 0이다.
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            return (i*2+j) * sz*sz + Z(x-sz*i, y-sz*j)

print(Z(2**N, r, C))

