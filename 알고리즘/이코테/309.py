"""
구현 - 문자열 압축

https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""

def solution(s):
    answer = len(s)
    for step in range(1, len(s) +1): # 1개 2개 3개 ... 단위로 자르기
        compressed = ""
        prev = s[0:step]
        count = 1 # 문자앞에 붙일 숫자
        for j in range(step, len(s), step):
            # prev와 같은 문자열이라면
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열일 경우(압축이 불가능)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 상태 초기화 다음 문자열
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed)) # 갱신
    return answer


assert solution("aabbaccc") == 7
assert solution("ababcdcdababcdcd") == 9
assert solution("abcabcdede") == 8
assert solution("abcabcabcabcdededededede") == 14
assert solution("xababcdcdababcdcd") == 17