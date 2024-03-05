"""
문서 검색
https://www.acmicpc.net/problem/1543

"""

a , b = input(), input()

count = 0
length = len(b)
start = 0
end = len(a) # 9
while start < end:
    current = a[start:start+length]
    if start > end - length:
        break
    if current == b:
        count += 1
        start += length
    else:
        start += 1
print(count)


## 또다른  정답 ##

while len(a) - start >= len(b):
    if a[start:start + len(b)] == b:
        count += 1
        start += len(b)
    else:
        start += 1

print(count)