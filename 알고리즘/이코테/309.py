"""
구현 - 문자열 압축

https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""

"""
만약 문자열이 8개라면 최대 4개단위까지 끊을 수 있다.
이유는 5개가 되면 최소 문자열이 10개가 필요하기 때문

만약 해당 문자열과 바로 뒤 문자열이 동일할 경우 count를 올려 새로운 문자열에 붙인다.
틀리다면, 해당 문자열 그대로 붙이고 다음 문자열로 이동한다.

그리고 마지막에 저장된 최종 문자열과 새로 들어온 문자열의 길이를 비교한다.
"""
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2+1):
        temp_str = ""
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                temp_str += str(count) + prev if count >= 2 else prev
                prev = s[i:i+step]
                count = 1
        temp_str += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(temp_str))
    return answer


assert solution("aabbaccc") == 7
assert solution("ababcdcdababcdcd") == 9
assert solution("abcabcdede") == 8
assert solution("abcabcabcabcdededededede") == 14
assert solution("xababcdcdababcdcd") == 17