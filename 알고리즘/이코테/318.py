"""
괄호 변환
https://school.programmers.co.kr/learn/courses/30/lessons/60058


1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""

def divide(p):
    # 2. 문자열 w를 두 균형잡힌 괄호 문자열 u,v로 분리
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            # u : 더 이상 분리할 수 없음, v : 빈 문자열이 될 수 있음
            return p[:i+1], p[i+1:] # u, v


def check(u):
    # 3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계 부터 다시 수행
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack: # ")" 이면서 안에 비었을 경우는 올바르지 않음.
                return False
            stack.pop()
    return True



def solution(p):
    # 1. 빈 문자열의 경우 빈 문자열을 반환
    if not p:
        return ""

    # 2
    u, v = divide(p)

    # 3
    if check(u):
        #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return  u + solution(v)
    
    else:
        # 4. 만약 올바른 문자열이 아닌 경우
        # 4-1. 빈 문자열에 첫 문자로 '('를 붙인다.
        answer = '('
        # 4-2. 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        answer += solution(v)
        # 4-3. 다시 ')'를 붙인다.
        answer += ')'
        # 4-4. u의 첫번째와 마지막 문자를 제거하고,
        for p in u[1:len(u) - 1]:
            # 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙인다.
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 4-5 생성된 문자열을 반환한다.
        return answer

assert solution("(()())()") == "(()())()", True
assert solution(")(") == "()", True
assert solution("()))((()") == "()(())()", True