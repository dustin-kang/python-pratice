from collections import deque
def solution(food_times, k):
    """
    1 ~ N 까지 음식을 섭취
    1초 동안 섭취 후 남은 음식 큐를 통해 뒤로 보내기
    K 때 까지 먹고난 후 다음 음식 번호 
    
    - 각 음식 당 시간 foodtimes
    - 장애 발생시간 K
    """
    answer = 1
    food_times = deque(food_times)
    length = len(food_times)
    while k>0:
        food = food_times.popleft()
        answer = (answer + 1) % length
        if food != 0:
            food -= 1
            food_times.append(food)
            k -= 1
        else:
            food_times.append(food)
            continue

    return answer

if __name__ == "__main__":
    print(solution([3, 1, 2], 5))