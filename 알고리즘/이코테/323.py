"""
정렬 - 국영수

12
Junkyu 50 60 100
Sankeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""

n = int(input())

result = []

for _ in range(n):
    name, k, e, m = map(str, input().split())
    k, e, m =int(k), int(e), int(m)
    result.append([name, k, e, m])

result.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(result[i][0])


# 최적화
for _ in range(n):
    # 리스트 형태로 result에 들어가게 된다.
    result.append(input().split())