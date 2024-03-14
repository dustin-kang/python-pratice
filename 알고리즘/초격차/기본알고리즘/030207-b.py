"""
트리의 높이와 너비
중(50분)
- 구현이 까다로운 문제
https://www.acmicpc.net/problem/2250

- 너비가 가장 넓은 레벨을 출력.
- 만약 동일한 레벨이 있다면 번호가 작은 레벨을 출력
"""

class Node:
    def __init__(self, number, left_node, right_node):
        """
        노드를 생성하는 클래스
        - parent : 부모노드
        - number : 값
        - left_node : 좌측 자식 노드
        - right_node : 우측 자식 노드
        """
        self.parent = -1 # 우선 부모 노드를 -1로 초기화  (-1일 경우 루트노드)
        self.number =  number
        self.left_node = left_node
        self.right_node = right_node

n = int(input()) # 노드의 개수
tree = {} # 트리 초기화
level_min = [n] # 해당레벨의 너비 최소값 초기
level_max = [0] # 해당레벨의 너비 최대값 초기
root = -1 # 루트노드 초기화
x = 1
level_depth = 1


for i in  range(1, n+1):
    # 해당 노드들을 초기회
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    # 데이터를 입력받아 트리 노드에 넣기
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node

    # 만약 자식노드에 데이터가 없다면 부모노드만 설정
    if left_node != -1: 
        tree[left_node].parent = number
    if right_node !=-1:
        tree[right_node].parent = number


# 부모노드가 없는 노드는 루트노드이므로 탐색
for i in range(1, n+1):
    if tree[i].parent == -1:
        root = i


def in_order(node, level):
    """
    ### 중위 순회
    - node : 노드
    - level : 해당 노드의 레벨
    """
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        # 만약 해당 노드에 좌측 자식노드가 있다면 (O)
        in_order(tree[node.left_node], level + 1)

    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1

    if node.right_node != -1:
        # 만약 해당 노드에 좌측 자식노드가 있다면 (O)
        in_order(tree[node.right_node], level + 1)


in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1

# 지식노드부터 너비 구하기
# 현재 레벨과 너비가 이전 레벨과 너비보다 크면 갱신화
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width


print(result_level, result_width)





