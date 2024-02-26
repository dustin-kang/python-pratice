"""
알파벳 찾기
20분
"""

alp_count = ord('z') - ord('a') + 1
alp = [-1] * alp_count

n = input()

for i in range(len(n)):
    index = ord(n[i]) - ord('a')
    if alp[index] == -1:
        alp[index] = i
    else:
        pass

for i in alp:
    print(i, end=' ')