"""
자물쇠와 열쇠
💡 좌물쇠의 크기를 3배인 리스트로 만들어 중간에 옮겨 좌물쇠의 합이 모두 1인지 확인한다.

https://school.programmers.co.kr/learn/courses/30/lessons/60059
"""
# 2.90도를 회전하는 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j] # 90도 회전
    return result

# 3. 좌물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    # 1. 좌물쇠 중앙 부분에 기존의 좌물쇠를 넣는다.
    n = len(lock)
    m = len(key)
    ## 좌물쇠의 크기를 기존의 3배로 바꾼다.
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    ## 중앙 부분의 기존 좌물쇠를 넣는다.
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4가지 방향(동서남북)에 대해 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전

        for x in range(n * 2):
            for y in range(n * 2):
                # 좌물쇠 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + 1][y + 1] += key[i][j]
                
                # 열쇠가 맞는지 확인하기
                if check(new_lock) == True:
                    return True
                # 열쇠가 맞지 않은 경우 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + 1][y + 1] -= key[i][j]
    return False


    

assert solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) == True