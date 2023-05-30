# stack\_queue

#### Stack과 Queue를 구현할 때 고민해야 하는 것

실제로 스택과 큐를 사용할 때 `Underflow` 와 `Overflow`를 고민해야 합니다.

* **`Underflow`** : 특정한 자료구조가 수용할 수 있는 데이터 크기가 가득찬 상태에서 삽입(push) 연산을 수행하는 것을 의미합니다.
* **`Overflow`** : 자료구조가 비어있는 상태에서 삭제(pop)연산을 수행할때 발생하는 것을 의미합니다.

![image](https://user-images.githubusercontent.com/55238671/235831698-cf4c6e89-7e45-4e91-be6b-2b81314d7f63.png)

## Stack

스택은 **FILO 방식**으로 하나의 동일한 입출구에서 마지막 데이터를 삭제 및 삽입할 수 있는 자료구조를 의미합니다.

#### 활용

1. **웹 브라우저 방문기록 확인** : 가장 최근에 열린 페이지 부터 확인
2. **역순 문자열 만들기** : 가장 나중에 입력된 문자 부터 출력
3. **실행 취소(undo, Command Z)** : 가장 최근 것 부터 실행 취소
4. **수식의 괄호 검사** (연산자 우선순위 표현을 위한 괄호 검사`(2+3)*4`)
5. **윈도우 프로그램** : 컴퓨터종료 시, 가장 먼저 운영체제가 구동되고 가장 마지막으로 종료된다.

* [👨‍💻 Stack Team Note](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/data-structure/stack.py)

## Queue

큐는 대기줄에 비유할 수 있습니다. 한쪽으로 삽입하면 반대 편에서는 삭제가 이루어지는 **FIFO 구조**입니다.

#### 활용

* 우선순위가 같은 작업 예약 (프린터의 인쇄 대기열)
* 은행 업무
* 콜센터 고객 대기시간
* 프로세스 관리
* **너비 우선 탐색(BFS, Breadth-First Search) 구현**
* **캐시(Cache) 구현**
* [👨‍💻 Queue Team Note](https://github.com/dustin-kang/Programming-Team-Notes/blob/Python/data-structure/queue.py)

> **📌 Queue 구현은 `Deque`를 사용하는 게 좋다.**
>
> `deque` 라이브러리는 스택과 큐의 장점을 모두 가지고 있는 라이브러리 입니다. 이유는 속도가 빠르고 간단히 이용할 수 있기 때문입니다.

```python
from collections import deque
data = deque([2,3,4])
data.appendleft(1) # 왼쪽에 1이라는 값을 추가
data.append(5) # 오른쪽에 5라는 값을 추가

print(data) # deque 객체 출력
print(list(data)) # 리스트 객체로 변환 후 출력
```
