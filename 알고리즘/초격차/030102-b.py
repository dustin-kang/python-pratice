"""
프린터 큐
https://www.acmicpc.net/problem/1966

- 입력
테스트 케이스
문서의 개수(1<=n<=100), 궁금한 문서의 순서(0<=M<N)
중요도(같은 문서가 여러 개 있을 수 있음)

- 풀이
현재 리스트에서 가장 큰수가 앞에 올 때까지 회전하면서 추출한다.
가장 큰수가 M이면서 가장 앞에 있다면 종료

"""

tc = int(input())
for i in range(tc):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    array = [(i, idx) for idx, i in enumerate(array)] # ✨ enumerate : idx, i

    count = 0

    while True:
        if array[0][0] == max(array, key=lambda x :x[0])[0]: # 가장 앞단 중요도가 가장 중요도 높은 값과 동일
            count += 1
            if array[0][1] == m: # 뽑은 값이 찾고자하는 값이라면
                print(count)
                break
            else:
                array.pop(0)
        else:
            array.append(array.pop(0)) # 앞에 원소를 뽑아 뒤로 추가



