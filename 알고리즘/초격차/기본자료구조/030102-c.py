"""
키로커
중(40분)
https://www.acmicpc.net/problem/5397

- 입력
테스트케이스
입력 문자

- : 백스페이스(앞글자 있다면 지우기)
<, > : 커서 위치 움직임
커서의 위치가 줄의 마지막이 아니라면 커서 오른쪽의 문자는 오른쪽으로 한칸 이동한다.

문자열의 크기가 최대 1,000,000이기 때문에 적절한 알고리즘을 설계해야한다.
"""

# 두개의 스택을 활용하는 것을 고민해야합니다.
"""
문자 입력 : 왼쪽 스택에 원소 삽입
- : 왼쪽 스택에서 원소 삭제
< : 왼쪽 스택에서 오른쪽으로 원소 이동
> : 오른쪽에서 왼쪽 스택으로 원소 이동

"""
tc = int(input())
for _ in range(tc):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    
    # 합치기
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))

