class Node:
    """
    싱글 연결 리스트
    """
    def __init__(self):
        """
        ### 노드를 생성하는 클래스
        - 연결리스트를 구현하기 전에 노드를 연결할 노드들을 생성합니다.
        """
        self.data = None
        self.next = None

    def printNode():
        """
        ### Node 전체 출력
        """
        node = head
        while node.next:
            print(node.data) # 중간 노드 데이터 출력
            node = node.next # 다음 노드로 넘김
        print(node.data) # 마지막 노드

    def add(data):
        """
        ### 마지막 노드에 노드를 추가하는 함수
        - `head` 노드 부터 시작하여 반복문(`while`)으로 다음 노드까지 도달
        - 마지막 노드의 경우 해당 노드 삽입
        """
        node = head
        while node.next: 
            node = node.next
        node.next = Node(data)

    def insert(find_data, insert_data):
        """
        ### 노드를 삽입하는 함수
        `find_data`, `insert_data`
        - 첫번째 `head` 노드에 삽입하는 방법
        - 중간 노드에 삽입하는 방법
        - 마지막 노드에 삽입하는 방법

        ```py
        node = Node()
        node.data = insert_data # 추가할 노드
        ```
        """
        # 첫번째 노드 삽입
        if head.data == find_data:
            node = Node()
            node.data = insert_data
            node.next = head
            head = node
            return
        
        # 중간 노드 삽입
        current_node = head
        while current_node.next != None: 
            pre_node = current_node # current_node 갱신하면서 뒤로 이동
            current_node = current_node.next
            if node.data == find_data:
                node = Node()
                node.data = insert_data
                # 추가할 노드의 다음 노드를 현재 노드로 설정
                node.next = current_node
                # 이전 노드의 다음 노드를 추가한 노드로 설정
                pre_node.next = node
                return
            
        # 마지막 노드 삽입
        node = Node()
        node.data = insert_data
        current_node.next = node

    def delete(delete_data):
        """
        ### 노드를 삭제하는 함수
        `delete_data`
        - 첫번째 `head` 노드를 삭제하는 방법
        - 이외에 방법

        ```py
        del(current_node)
        ```
        """
        current_node = head # 헤드 노드를 우선 현재 노드로 설정
        if head.data == delete_data:
            head = head.next # 후행 노드를 head로 설정
            del(current_node) # 현재노드(전 head 노드) 삭제
            return
        
        while current_node != None:
            pre_node = current_node # current_node 갱신하면서 뒤로 이동
            current_node = current_node.next
            # 삭제할 노드가 현재 노드의 경우
            if current_node.data == delete_data:
                pre_node.next = current_node.next
                del(current_node)
                return
    
    def search(find_data):
        """
        ### 검색할 노드 찾는 함수
        `find_data`
        """
        current_node = head # 헤드 노드를 우선 현재 노드로 설정
        if current_node.data == find_data:
            return current_node
        while current_node.next != None:
            current_node = current_node.next
            if current_node.data == find_data:
                return current_node
        return Node() # 빈 노드 반환

class Node2():
    """
    이중 연결 리스트
    """
    def __init__(self) -> None:
        self.pre = None
        self.data = None
        self.next = None

    def printNodes(start):
        current_node = start
        if current_node.next == None:
            return
        print(current_node.data, end='')
        while current_node.next != None:
            current_node = current_node.next
            print(current_node.data, end=" ")
        print()
        while current_node.pre != None:
            current_node = current_node.pre
            print(current_node.data, end=" ")


dataArray = [i for i in range(1, 10)]

if __name__ == "__main__":
    # 노드 생성
    node = Node()
    node.data = dataArray[0]
    head = node

    # 노드 연결
    for data in dataArray[1:]:
        pre_node = node
        node = Node()
        node.data = data
        pre_node.next = node


