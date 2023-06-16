# 데이터 클래스

## 데이터 클래스

이전에 클래스에서 변수를 반복해서 작성해야한다는 chore이 있었습니다. 수정 없이 반복적으로 사용하는 코드를 작성해야 했습니다. 이를 **보일러 플레이트(Boiler Plate) 코드** 라고도 하죠.

> #### 보일러 플레이트 코드(Boiler Plate Code)
>
> 코드의 수정없이 반복적으로 사용하는 코드로 재사용하여 단순 작업 시간을 덜어주는 코드입니다. 대표적으로 `if __name__ = "__main__"`이 있죠.

![image](https://user-images.githubusercontent.com/55238671/239812324-8edea60b-2146-423a-9591-9c3e53e6f6fa.png)

다시 본론으로 넘어가서, 위 그림 처럼 일반 클래스에 `@dataclass`를 선언해주면 `__init__()`, `__repr__()`, `__eq__()`와 같은 메서드를 따로 작성할 필요 없이 자동으로 생성이 됩니다.

여기서 클래스를 좀 더 잘 활용할 수 있는 강력한 기능이 있습니다.

#### 불변 데이터 만들기 `frozen`

`frozen`이라는 옵션을 사용하면 데이터를 불변(immutable)하게 만들 수 있습니다. 데이터 클래스가 담고 있는 `admin`과 같은 데이터를 변경하면 예외가 발생하게됩니다.

```python
class User(frozen=True):
```

#### 인스턴스 간 대소 비교 `order`

`order` 옵션을 사용하면 인스턴스 간 대소 비교가 가능합니다. 또한 `sorted([instance1, instance2])`를 통해 정렬도 가능합니다.

```python
class User(order=True):

user1 > user2
```

#### 세트나 사전으로 사용하기 `unsafe_hash` `asdict` `astuple`

Hashable하게 사용하기 위해 `unsafe_hash` 옵션을 사용하여 set 자료형으로 만들 수 있어 중복된 데이터가 있는 인스턴스를 제거할 수 있습니다.

```python
from data classes import dataclass, astuple
class User(unsafe_hash=True):
...

set([user1, user2, user3])

# print(astuple(user2))
```

#### 인스턴스 데이터 수정하기 `replace`

```python
from data classes import dataclass, replace
print(replace(user1, id='no3'))
```

#### 상속 및 List 화 하기

```python
from dataclasses import dataclass
from typing import List


@dataclass
class Inventory:
    user: List[User]

inventory = Inventory([user1, user2])

# inheritance
@dataclass(frozen=True)
class Taxi(Car):
    owner_company: str = ""

taxi1 = Taxi(1, "YELLOW", "HYUNDAI", "xyz")
print(taxi1)
```

여기서 List를 생성할 때 기본값을 할당할 수 없습니다. 이유는 필드의 기본 값은 인스턴스 간에 공유되기 때문입니다. 그래서 `field(default_factory=list)`를 사용해야 합니다. `List[int] = field(default_factory=list)`

* [Data Classes](https://docs.python.org/3/library/dataclasses.html)
* [\[파이썬\] 데이터 클래스 사용법 (dataclasses 모듈) - DaleSeo](https://www.daleseo.com/python-dataclasses/)
