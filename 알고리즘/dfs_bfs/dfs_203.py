"""
백트래킹
DFS
A,B,C 세사람이 각자 가지고 있는 숫자들을 하나씩 줄 세운다고 가정했을 때,
 짝수나 홀수가 연속으로 나오면 안되는 조건입니다. 
이때, 만들 수 있는 숫자를 모두 구하면 됩니다. (순서는 A-B-C)

"""

# A,B,C 숫자들을 2차원 배열에 차례대로 넣습니다.
numbers = [[1,2,3],[4,5,6],[7,8,9]]

def dfs(numbers, depth, answer, history):
    if depth == len(numbers):
        answer.append(history[:])
        return 

    if not history:
        for n in numbers[depth]:
            new_history = history[:]
            new_history.append(n)
            dfs(numbers, depth + 1, answer, new_history)
    else:
        for n in numbers[depth]:
            if history[-1] % 2 == 0 and n % 2 != 0:
                new_history = history[:]
                new_history.append(n)
                dfs(numbers, depth + 1, answer, new_history)

            if history[-1] % 2 != 0 and n % 2 == 0:
                new_history = history[:]
                new_history.append(n)
                dfs(numbers, depth + 1, answer, new_history)

    return answer


def solution(numbers):
    answer = []
    return dfs(numbers, 0, answer, [])

print(solution(numbers))
