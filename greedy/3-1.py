"""
모험가 길드
"""

# 문제 풀이

n = int(input()) # 모험가 수를 입력 받는다.
members = list(map(int, input().split(' '))) # 모험가들을 입력 받아 리스트에 저장한다.
i = 0 # 인덱스
answer = 0 # 결과

members.sort(reverse=True) # 공포도가 높은 순서대로 정렬한다.
while n >= 0: # 모험가 수가 그룹 수보다 작거나 동일 할 때 까지
    n -= members[i]  # 가감
    answer += 1 # 가감할 수록 그룹 수 추가

print(answer)

# 정답

n = int(input()) # 모험가 수를 입력 받는다.
members = list(map(int, input().split(' '))) # 모험가들을 입력 받아 리스트에 저장한다.
members.sort() # 공포도가 낮은 순서대로 정렬한다.

answer = 0 # 그룹 수
count = 0 # 그룹에 포함된 모험가 수

for i in members: # 공포도가 낮은 것 부터 하나씩 확인
    count += 1 
    if count >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상의 경우
        answer += 1
        count = 0 # 초기화
print(answer)
