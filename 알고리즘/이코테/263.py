"""
정렬 - 성적이 낮은 학생대로 출력하기

2
홍길동 95
이순신 77
"""

n = int(input())
a = [tuple(input().split()) for _ in range(n)]

a.sort(key=lambda x: x[1])

for i in a:
    print(i[0])