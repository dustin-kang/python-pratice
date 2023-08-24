class Node(object):
    """
    ### 노드 클래스 만들기
    - `value` : 노드의 값(데이터)
    - `left` : 왼쪽 노드의 정보 `None`
    - `right` : 오른쪽 노드의 정보 `None`
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BST(object):
    """
    ### 이진 탐색 트리
    """
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """
        ### 이진 트리에 데이터 삽입
        - `value` : 값
        """
        self.root = self._insert_value(self.root, value)
        return self.root is not None

    def  _insert_value(self, node, value):
        """
        삽입 절차 (`node` `데이터`)
        - 만약 노드가 존재하지 않은 경우
            : 노드로 지정한다.
        - 삽입된 데이터(`value`)가 노드 데이터(`node`)보다 작은 경우
            : 왼쪽 노드에 넣는다.
        - 삽입된 데이터(`value`)가 노드 데이터(`node`)보다 큰 경우
            : 오른쪽 노드에 넣는다.
        """
        if node is None:
            node = Node(value)
        else:
            if value <= node.value:
                node.left = self._insert_value(node.left, value)
            else :
                node.right  = self._insert_value(node.right, value)
        return node
    
    def find(self, value):
        """
        ### 이진 트리에서 데이터 찾기
        - `value`: 값
        """
        return self._find_value(self.root, value)
    
    def _find_value(self, root, value):
        """
        팀색 절차 ('root'(해당 트리의 루트 역할), `value`(찾을 데이터))
        - 루트 노드가 존재하지 않거나 해당 데이터 값이 루트 노드 값과 일치하는 경우
            : 루트노드 반환
        - 값이 루트 노드보다 작은 경우
            : 왼쪽 탐색
        - 값이 루트 노드보다 큰 경우
            : 오른쪽 탐색
        """
        if root is None or root.value == value:
            return root is not None
        elif value < root.value:
            return self._find_value(root.left, value)
        else:
            return self._find_value(root.right, value)

    def delete(self, value):
        """
        ### 이진 트리에서 데이터 제거
        - `value`: 값
        """
        self.root, deleted = self._delete_value(self.root, value)
        return deleted
    
    def _delete_value(self, node, value):
        """
        ### 제거 절차(`node` `데이터`) -> (`제거된 노드`, `제거여부T/F`)
        - 노드가 존재하지 않는 경우
            : 데이터를 제거할 수 없음 `False` 반환
        - 데이터가 노드와 동일한 경우 (찾는 데이터가 맞는(`True`) 경우!)
            - 왼쪽, 오른쪽 노드 모두 있는 경우(`and`)
                오른쪽 노드가 노드가 되고 왼쪽노드가 오른쪽 노드의 자식이 됨
            - 왼쪽, 오른쪽 노드 중 하나라도 있는 경우(`or`)
                둘 중에 하나를 노드로 대입
            - 둘다 없는경우( 노드만 있는 경우)
                노드 제거(`None`)
        - 데이터가 노드보다 작은 경우
            : 왼쪽으로 이동해 제거 절차 진행
        - 제거할 데이터가 노드보다 큰 경우
            : 오른쪽으로 이동해 제거 절차 진행
        """
        if node is None:
            return node, False
        
        deleted = False

        if value == node.value:
            deleted=True
            if node.left and node.right:
                # 노드의 자식노드가 노드되야하는 상황
                parent, child = node, node.right

                # 자식의 왼쪽노드가 없어질 때까지 자식이 부모되고 반복
                while child.left is not None:
                    parent, child = child, child.left
                # 노드의 왼쪽이 자식(기존 노드의 오른쪽)의 왼쪽으로 들어감
                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif value < node.value:
            node.left, deleted =  self._delete_value(node.left, value)
        else:
            node.right, deleted = self._delete_value(node.right, value)
        return node, deleted
    
    def DFTravel(self):
        """
        ### 전위 순회
        루트 -> 왼쪽 -> 오른쪽
        """
        def _DFTravel(root):
            """
            ### 전위 순회
            루트(출력) -> 왼쪽 -> 오른쪽
            """
            if root is None:
                pass
            else:
                print(root.value, end = " - ")
                _DFTravel(root.left)
                _DFTravel(root.right)
        _DFTravel(self.root)

    def LFTravel(self):
        """
        ### 중위 순회
        왼쪽 -> 루트(출력) -> 오른쪽
        """
        def _LFTravel(root):
            """
            ### 중위 순회
            왼쪽 -> 루트(출력) -> 오른쪽
            """
            if root is None:
                pass
            else:
                _LFTravel(root.left)
                print(root.value, end = " - ")
                _LFTravel(root.right)
        _LFTravel(self.root)

    def LRTravel(self):
        """
        ### 후위 순회
        왼쪽 -> 오른쪽 -> 루트(출력)
        """
        def _LRTravel(root):
            """
            ### 후위 순회
            왼쪽 -> 오른쪽 -> 루트(출력)
            """
            if root is None:
                pass
            else:
                _LRTravel(root.left)
                _LRTravel(root.right)
                print(root.value, end = " - ")
        _LRTravel(self.root)     

    def layerTravel(self):
        """
        ### 레벨 순회
        순차적으로 왼쪽부터 queue 자료구조에 데이터를 넣어 꺼내 출력하는 방식
        """
        def _layerTravel(root):
            """
            ### 레벨 순회
            순차적으로 왼쪽부터 queue 자료구조에 데이터를 넣어 꺼내 출력하는 방식
            """
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.value, end= " - ")
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _layerTravel(self.root)  




########
data = [20, 6, 8, 12, 78, 32, 65, 32, 7, 9]
tree = BST()

# 데이터를 삽입해 트리구조 완성시키기
for x in data:
    tree.insert(x)

# 트리 내 데이터 존재 확인
print(tree.find(9)) # True
print(tree.find(3)) # False

print(tree.delete(78)) # True
print(tree.delete(6)) # True
print(tree.delete(11)) # False

# 트리 구조 데이터 출력

print("\n전위순회")
tree.DFTravel()

print("\n중위순회")
tree.LFTravel()
print("\n후위순회")
tree.LRTravel()
print("\n레벨순회")
tree.layerTravel()