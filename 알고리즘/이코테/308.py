"""
구현 - 문자열 재정렬

K1KA5CB7 -> ABCKK13

AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20

"""

data = input()
num_result = 0
str_result = []

for i in data:
    if i.isalpha():
        str_result.append(i)
    else:
        num_result += int(i)
        
str_result.sort
str_result.append(str(num_result))
print(''.join(str_result))
