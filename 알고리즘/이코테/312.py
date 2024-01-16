"""
기둥과 보 설치
https://school.programmers.co.kr/learn/courses/30/lessons/60061

설치와 삭제를 나눠서 진행하는 것은 맞다.
여기서 중요한 것은 "전체 구조물을 확인한다"는 규칙이다.
"""

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥의 경우
            if y == 0 or \
               [x - 1, y, 1] in answer or \
               [x, y, 1] in answer or \
               [x, y - 1, 0] in answer:
                continue
            return False # 정상이 아니라면 False
        else: # 보의 경우
            if [x, y - 1, 0] in answer or \
               [x + 1, y - 1, 1] in answer or \
               [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                continue
            return False
    return True 

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x,y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        else:
            answer.append([x,y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)   
