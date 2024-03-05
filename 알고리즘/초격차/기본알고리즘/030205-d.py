"""
트로피 진열
https://www.acmicpc.net/problem/1668

"""

n = int(input()) # 트로피 개수
array = []

for i in range(n):
     array.append(int(input()))

# 왼쪽에서 봤을 때 첫번째 수가 두번쨰 수보다 작으면 1씩 증가 
# 오른쪽에서 봤을 떄 마지막 수가 막 -1 번째 수보다 작으면 1씩 증가

def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:  
            result += 1
            now = array[i] 
    return result

print(ascending(array))
array.reverse()
print(ascending(array))