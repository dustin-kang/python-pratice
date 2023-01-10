def solution(brown, yellow):
    answer = []
    
    sum = brown + yellow
    
    # 3,4 / 4,3 / 5,2.4 / 6,2
    for i in range(3, int(sum / 2) + 1):
        j = sum / i
        
        # 소수점이 있는 수는 타일 갯수로 변환하기 어렵기 때문
        if (j * 10) % 10 != 0:
            continue
        
        # 노란색이 있는 사각형 타일을 만들기 위해 갈색 타일을 제거한다.
        if (i - 2) * (j - 2) == yellow: 
            answer.append(i)
            answer.append(int(j))
            break
    
    # 가로 길이는 세로 길이와 같거나 세로 길이보다 길어야 한다.
    if answer[0] < answer[1]:
        swap = answer[0]
        answer[0] = answer[1]
        answer[1] = swap

    return answer
