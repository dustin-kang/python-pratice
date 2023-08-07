class Heap:
    def __init__(self):
        """
        힙(Heap) 생성
        """
        self.heap = []
        self.heap.append(None)

    # 노드 삽입
    ## 해당 노드가 부모노드보다 큰지 비교
    def check_swap_push(self, idx):
        # 해당 노드의 부모노드가 없는 경우
        if idx <= 1:
            return False
        # 해당 노드의 부모노드 : idx // 2
        parent_idx = idx // 2

        # 부모노드보다 값인 큰 경우 Swap 가능
        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False
        
    def push(self, data):
        """
        ### 데이터 삽입하기
        1. 새로 들어온 데이터는 마지막 노드(idx)로 설정한다.
        2. 부모노드보다 큰지 확인하면서(`check_swap`)
        3. `True`인 경우 부모노드와 자식 노드가 교체됩니다.
        """
        self.heap.append(data)
        # 새로 들어온 데이터는 마지막 노드
        idx = len(self.heap) - 1

        while self.check_swap_push(idx):
            parent_idx = idx // 2
            # swap
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        return True
    
    # 노드 삭제
    def check_swap_pop(self, idx):
        # 자식 노드들의 인덱스
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        # 자식 노드가 없을 경우(자식 노드 인덱스가 힙의 길이보다 클 경우)
        if left_idx >= len(self.heap):
            return False
        
        # 왼쪽 자식 노드만 있는 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
        
        # 왼쪽, 오른쪽 모두 있을 경우
        else:
            # 왼쪽 자식노드가 더 큰 경우
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    self.flag = 1 # 왼쪽 자식노드
                    return True
                else:
                    return False
            # 오른쪽 자식노드가 더 큰 경우
            else:
                if self.heap[right_idx] > self.heap[idx]:
                    self.flag = 2 # 오른쪽 자식 노드
                    return True
                else:
                    return False
            
    def pop(self, idx):
        """
        ### 데이터 삭제하기
        1. 삭제할 데이터는 최상단 노드로 설정한다.
        2. 자식노드보다 큰지 확인하면서(`check_swap`)
            - 자식노드가 없는 경우
            - 왼쪽 자식노드만 있는 경우
            - 왼쪽 오른쪽 자식노드 모두 있는 경우 -> 두 자식 노드는 크든 작든 상관 없음
        3. `True`인 경우 부모노드와 자식 노드가 교체됩니다.
        """
        # pop할 데이터가 없는 경우
        if len(self.heap) <= 1:
            return None
        
        # 최댓값 데이터 빼내기
        max = self.heap[1]
        # 마지막 데이터 값을 최상단으로 변경하기
        self.heap[1] = self.heap[-1]
        del self.heap[-1] # 마지막 데이터는 제거
        idx = 1

        self.flag = 0

        while self.check_swap_pop(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            # 왼쪽 자식노드 또는 오른쪽 자식노드와 교환
            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        return max
