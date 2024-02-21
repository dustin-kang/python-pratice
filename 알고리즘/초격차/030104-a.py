"""
오큰수
50분
https://www.acmicpc.net/problem/17298

- 오큰수 : 오른쪽에 있으면서 A_i보다 큰 수중 가장 왼쪽에 있는 수
A = [3, 5, 2, 7]의 경우 NGE(1) = 5, NGE(2) = 7, NGE(4) = -1

- 수열에 값을 담을 때 오큰수도 같이 기록해주면 된다.

"""

n = int(input())
array = list(map(int, input().split()))
nge = [-1] * n
stack = []

for i in range(n):
    x = array[i]
    # 내림차순일 때(다음수가 작을 때)
    if len(stack) == 0 or stack[-1][0] >= x:
        stack.append((x, i)) # 수, 인덱스
    # 오름차순일 때(다음수가 클 때)
    else:
        while len(stack) > 0: 
            previous, index = stack.pop()
            if previous >= x: 
                # 이전 수가 더 큰 경우 9,.., 8
                stack.append((previous, index))
                break
            else:
                #이전 수 가 더 작은 경우 4, 8
                nge[index] = x # 이전 인덱스에 오큰수 기록
        stack.append((x, i)) # 다음을 위해 다시 해당 인덱스와 값 담기

for x in nge:
    print(x, end=' ')





