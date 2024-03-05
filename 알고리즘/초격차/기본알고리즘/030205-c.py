"""
베스트 셀러
https://www.acmicpc.net/problem/1302
"""

n = int(input())

books = dict()
for i in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())
array = []

# 같은 Max 중 사전순으로 가장 앞에 있는 책
for book, number in books.items():
    if number == target:
        array.append(book)

print(sorted(array)[0])
