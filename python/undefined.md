# 가변객체와 불변 객체

## 가변 객체와 불변 객체

우선 모든 객체들은 **값(value), 유형(type), 정체성(id)** 라는 세가지 특징을 가지고 있습니다.

* **Value** : 메모리에 저장된 값
* **Type** : 객체의 데이터 타입, 객체의 생성자
* **id** : 일종의 고유한 메모리 주소로 `a is b` 로 확인이 가능

<figure><img src="https://user-images.githubusercontent.com/55238671/232321133-e9bbb48a-f6b6-4948-a3e0-59a449c44a52.png" alt=""><figcaption></figcaption></figure>

```python
print(isinstance('this is string'), str)
print(isinstance(['this', 'is', 'list'], list)
```

그 객체들은 또 생성자(클래스)에 따라 가변 객체와 불변 객체로 나뉘게 됩니다.

* **가변 객체(mutable object)** : list, dict, set
* **불변 객체(immutable object)** : int float, string, bool, **tuple** (값이 바뀌지 않는 변수)

<figure><img src="https://user-images.githubusercontent.com/55238671/230564262-158b9a01-e1c0-48ac-9f52-749183fe03d4.png" alt=""><figcaption></figcaption></figure>

## 2️⃣ 할당 연산자 (`=`; Assignment Operator)

할당 연산자는 두 변수를 메모리의 한 목록을 가리키게 합니다. 복사본을 만드는 게 아닙니다.

아래 예시를 보게되면, `colors` 라는 변수가 리스트를 참조하게 되고 `b`는 colors 주소를 복사하게 됩니다. 이후, `b`라는 변수에 새로운 값이 추가하게되면 `colors`에도 값이 추가되는 것이죠. 즉, **주소(Adress)를 복사하는 것을 할당(Assignment)한다**라고 합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235280257-d4281ac1-6e28-4b0a-8d06-54b810327602.png" alt="" width="375"><figcaption></figcaption></figure>

그렇다면 `copy`는 무슨 의미일까요?

### Shallow Copy

위 설명을 보시면 새로운 복합 객체를 구성한다음, **원본 객체에서 발견된 객체에 대한 참조**를 삽입한다고 합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235281094-31646ae0-9550-4fd3-ba92-682ba1b64f84.png" alt="" width="375"><figcaption></figcaption></figure>

우선, 할당과는 새로운 객체를 만든다는 차이가 있습니다. 그래서 원래 목록을 변경하거나 추가하는 것에 영향을 미치지 않습니다. 하지만, 리스트 내 가변 객체를 수정하면, 원본 객체도 반영이 된다는 것입니다.

```python
# list.copy() == list[:]

a = [[1, 2], [2, 4]]
b = a[:] ## shallow copy

b.append([3, 6]) # [[1, 2], [2, 4], [3, 6]]
print(b, a) # a = [[1, 2], [2, 4]]

b[0].append(3) ## Edit the first element (i.e. [1, 2])
print(b, a) # a, b = [[1, 2, 3], [2, 4]]
```

### Deep Copy

위 Shallow Copy와 동일하게 새로운 복합 객체를 구성하지만, 참조하지 않고 **원본 객체를 완전히 복사** 합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235281167-3ed10fd9-b7ec-4a07-8e21-7e1035a0c721.png" alt="" width="375"><figcaption></figcaption></figure>

```python
a = [[1, 2], [2, 4]]
import copy
b = copy.deepcopy(a) ## deep copy
b[0].append(4)
print(b) # [[1, 2, 4], [2, 4]]
print(a) # [[1, 2], [2, 4]]
```

### 불변 객체의 Copy

> 파이썬의 변수는 **C언어** 처럼 변수를 **메모리에 바로 저장**하지 않습니다. **파이썬**은 값이 있는 <mark style="color:orange;">객체를 메모리 힙 영역에 저장하고</mark> <mark style="color:orange;"></mark><mark style="color:orange;">**변수가 그 객체를 가리키는 것**</mark><mark style="color:orange;">입니다.</mark>

```python
x = 'test'
y = x
print(x is y) # True

x = x + ' modified'
print(x is y) # False
```

### 가변 객체의 Copy

* 가변 객체는 Item Assignment도 지원하는데 이는 가변 객체의 원소가 변경되어도 id는 바뀌지 않는다는 의미입니다.
* copy : 가변객체는 메모리 주소 값을 직접 Point하는 게 아니라 **pointer만 복사**하는 것입니다.
* deep copy : DEEP하게 복사했으니 **주소값도 변경**됩니다.

```python
from copy import deepcopy

x = [1,2,3]
y = x

print(x is y) # True

x += [4, 5]
print(x is y) # True

print(x) # [1,2,3,4,5]
print(y) # [1,2,3,4,5]

y = deepcopy(x)

print(id(x)
print(id(y)
```

### 우리가 알아야하는 이유?

불변 객체와 가변 객체의 연산 비교하면 <mark style="color:blue;">**불변 객체**</mark>는 매번 새로운 메모리 공간을 할당해주어야 하기 때문에 <mark style="color:blue;">**메모리 누수 발생 가능성**</mark>이 있습니다.

하지만 <mark style="color:blue;">**불변 객체는 값이 변하지 않는다는 점에서 신뢰성이 높습니**</mark><mark style="color:blue;"><mark style="color:red;">**다.**<mark style="color:red;"></mark>&#x20;

#### Reference.

[https://towardsdatascience.com 블로그](https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a)

[불타는 코딩 블로그](https://fierycoding.tistory.com/43)

[Python:Assignment vs Shallow Copy vs Deep Copy - Thawsitt Naing](https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86)

[파이썬 interning](http://pythonstudy.xyz/python/article/512-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Object-Interning)
