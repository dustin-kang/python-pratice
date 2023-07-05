class Stack():
    """
    FILO 방식의 하나의 동일한 입출구에서 데이터를 삭제 및 삽입할 수 있는 자료구조 입니다.
    
    - functions
        - push(element) : 삽입 연산
        - pop() : 삭제 연산
        - top() : 가장 상단 데이터 출력
    - params
        - length : 수용가능한 데이터 크기를 설정합니다.
    """
    def __init__(self, length=int):
        self.stack = list()
        self.length = length

    def push(self, element):
        """
        `push` : 삽입 연산
        - 가장 상단에 요소를 추가합니다.
        - 수용 데이터 크기를 초과한 경우 `Overflow`를 출력합니다.
        """
        if len(self.stack) == self.length:
            print("Overflow")
        else :
            self.stack.append(element)
            print(self.stack)

    def pop(self):
        """
        `pop` : 삭제 연산
        - 가장 상단에 있는 요소를 삭제합니다.
        - 만약 스택의 요소가 없는 경우 `Underflow`를 출력합니다.
        """
        if len(self.stack) < 1:
            print("Underflow")
        else :
            del self.stack[-1]
            print(self.stack)

    def top(self):
        """
        가장 상단에 있는 요소를 출력합니다.
        """
        if len(self.stack) < 1:
            print("Underflow")
        else:
            print(self.stack[-1])
            return self.stack[-1]
