"""
스택 수열
https://www.acmicpc.net/problem/1874

- 삽입 : 특정 수에 도달할 때 까지 삽입
- 삭제 : 내림차 순 유지 확인

"""

n = int(input())
count = 1
stack = [] 
result = [] # + -

for _ in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때
        stack.pop()
        result.append('-')
    else:
        print("NO") # 내림차 순이 아니면 뽑을 수 없음
        exit(0) # 종료

print('\n'.join(result))


