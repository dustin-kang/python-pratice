import random

# 알파벳
lower_alphabets = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
upper_alphabets = []
for alphabet in lower_alphabets:
  upper_alphabets.append(alphabet.upper())
alphabets = lower_alphabets + upper_alphabets
# print(alphabets)

# 수
numbers = [str(i) for i in range(0, 10)]

# 특수 문자
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 컴스텀할 문자, 수, 특수문자
num_of_alphabets = 9
num_of_numbers = 3
num_of_symbols = 2

strong_password = []

# 패스워드 랜덤 생성
for i in range(0, num_of_alphabets):
  strong_password.append(alphabets[random.randint(0, len(alphabets) - 1)])

for i in range(0, num_of_numbers):
  strong_password.append(numbers[random.randint(0, len(numbers) - 1)])

for i in range(0, num_of_symbols):
  strong_password.append(symbols[random.randint(0, len(symbols) - 1)])

random.shuffle(strong_password)

print("".join(strong_password))