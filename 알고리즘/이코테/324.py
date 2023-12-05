'''
정렬 - 안테나

6
1 2 3 5 8 9

3
'''

n = int(input())

data = list(map(int, input().split()))
data.sort()

# 중간값  출력
print(data[(n-1)//2])