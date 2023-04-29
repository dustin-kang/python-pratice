question = list("hangman")
lst = ['_' for i in range(len(question))]
num_of_try = 10

while True:
    char = input("Guess the char?")
    i = 0
    for elem in question: # 문자 하나하나 맞는지 검토 하기
        if elem == char: 
            lst[i] = char
        i += 1
    print(lst)

    if '_' not in lst: # 이길 경우
        print("You Won!")
        break
    if num_of_try < 1: # 질 경우
        print("You lost")
        print(f"question")
        break
    num_of_try -= 1
    
