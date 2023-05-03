class Queue():
    """
    FIFO 방식으로 한쪽으로 삽입하면 반대 편에서 삭제가 이루어지는 자료구조입니다.
    
    - functions
        - push(element) : 삽입 연산
        - pop() : 삭제 연산
        - rear() : 가장 상단 데이터 출력
        - front() : 가장 하단 데이터 출력
    - params
        - length : 수용가능한 데이터 크기를 설정합니다.
    """
    def __init__(self, length=int):
        self.queue = list()
        self.length = length

    def push(self, element):
        """
        `push` : 삽입 연산
        - 가장 상단에 요소를 추가합니다.
        - 수용 데이터 크기를 초과한 경우 `Overflow`를 출력합니다.
        """
        if len(self.queue) == self.length:
            print("Overflow")
        else :
            self.queue.append(element)
            print(self.queue)

    def pop(self):
        """
        `pop` : 삭제 연산
        - 가장 하단에 있는 요소를 삭제합니다.
        - 만약 스택의 요소가 없는 경우 `Underflow`를 출력합니다.
        """
        if len(self.queue) < 1:
            print("Underflow")
        else :
            del self.queue[0]
            print(self.queue)

    def rear(self):
        """
        가장 상단에 있는 요소를 출력합니다.
        """
        if len(self.queue) < 1:
            print("Underflow")
        else:
            print(self.queue[-1])
            return self.queue[-1]

    def front(self):
        """
        가장 하단에 있는 요소를 출력합니다.
        """
        if len(self.queue) < 1:
            print("Underflow")
        else:
            print(self.queue[-1])
            return self.queue[-1]
    