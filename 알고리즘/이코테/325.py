"""
정렬 - 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889

실패율  : 스테이지에 도달은 했으나 클리어를 못한 사람 / 스테이지에 도달한 사람
"""
def solution(N, stages):
    answer = {}
    players = len(stages)
    for i in range(1, N+1):
        if players != 0:
            clears = stages.count(i)
            answer[i] = clears / players # 실패율
            players -= clears # 실패한 사람 만큼 가감
        else:
            answer[i] = 0
        print(answer)

    # 딕셔너리 번호의 순서대로 정렬
    return sorted(answer, key= lambda x : answer[x], reverse=True)

    

assert solution(5, [2,1,2,6,2,4,3,3]) == [3,4,2,1,5]
assert solution(4, [4,4,4,4]) == [4,1,2,3]