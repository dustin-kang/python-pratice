# 클래스

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption><p>Class</p></figcaption></figure>

## 클래스

> 아래 예제는, Pypi(파이썬 레지스트리)사이트에서 `PrettyTable`라는 패키지를 불러왔습니다.

```python
from prettytable import PrettyTable

x = PrettyTable()
# Attribute
x.field_names = ['City name', 'Area', 'Population', 'Anuual Rainfall'] # column_name
# Method
x.add_row(['Adelaide', 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
print(x)

print(vars(x)) # vars()라는 함수를 사용하면 Object가 어떤 속성들을 가지고 있는지 확인할 수 있습니다.
```

> #### Class의 Name Convention
>
> * PascalCase : 클래스 이름 정의할 때 사용
> * camelCase : 오브젝트를 정의할 때 사용
> * snake\_case : 그외 함수등을 정의할 때 사용

### 클래스의 생성자(Construction)

> 클래스를 생성하는 **동시에 호출**되는 함수

```python
class Car:
    def __init__(self): # Constructor
        self.color = 'red' # self : 현재 자신이 가지고 있는 오브젝트
        self.engine_type = "electric"

tesla = Car()
print(tesla.color)
```

* 생성자 파라미터에 매개변수를 지정해주면 인스턴스화 할 때 파라미터를 지정해줄 수 있습니다.
* 생성된 클래스 인스턴스는 각각의 메모리에 저장됩니다. `id`가 다릅니다.

### 상속(Inheritance)

기존 부모 클래스의 속성과 메소드가 자식 클래스에도 사용할 수 있습니다.

* <mark style="color:orange;">**`super()`**</mark> 메소드를 사용하면 <mark style="color:orange;">**부모가 가지고 있는 메소드를 사용**</mark>할 수 있습니다.
* <mark style="color:orange;">**메소드 오버라이드**</mark> : 부모 클래스의 메소드 명과 자식 클래스의 메소드 명이 **동일한 경우, 새롭게 재정의**합니다.

```python
class Car:

    def __init__(self):
        self.wheel_count = 4
        self.door_count = 2

    def start(self):
        print("started...")

    def drive(self):
        print("driving...")


class ElectricCar(Car):

    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print("No sound ...")

ec = ElectricCar()
ec.start()
ec.drive()
```

### 메소드

#### Instance Method

* 매개변수로 객체(object, self)를 사용합니다.

```python
class Car:
    def set_body_type(self, body_type):
        self.body_type = body_type
```

#### Class Method

> 클래스를 Object화 할때 사용하는 메소드입니다.

* Factory Method를 사용할 때 쓰입니다.
* 아래 예제를 보면 `Car`라는 클래스가 `cls`를 치환하여 출력합니다.

```python
class Car:
    @classmethod
    def hyundai(cls):
        return cls("sedan")
```

#### Static Method

> 인스턴스나 클래스에 **전혀 연관되어있지 않은 메소드**입니다.

* 굳이 Object를 생성할 필요 없이 만들 수 있는 메소드입니다.
* `@staticmethod` 데코레이터를 사용할 수 있습니다.

```python
class Calc:
    def add(x: int, y: int) -> int:
        return x + y

# create addNumbers static method
Calc.add = staticmethod(Calc.add) # 데코레이터를 사용하면 오브젝트를 만들어 줄 필요 없다.

print('Product:', Calc.add(15, 110))
```

#### 스페셜 메소드(Magic Method)

파이썬에 있는 여러 내장 함수들이 호출하는 메소드를 **새로 커스텀하여 정의**할 수 있습니다.

* 예를 들어서, `__len__()`이라는 스페셜 메서드를 정의하면 `len()` 내장함수를 사용할 수 있습니다.
* 앞 뒤에 `__` 언더바 두개를 붙여 던더 메서드(dunder method)를 사용합니다.

<pre class="language-python"><code class="lang-python">class Tesla(object):

    def __init__(self, owner, color):
        self.owner = owner
        self.color = color

    def __str__(self): # 서로 다른 자료형 간의 인터페이스를 출력하는 메소드
        return f"This is {self.color} color {self.owner}'s car"

    def __len__(self): # len() 함수를 반환할 때 사용하는 메소드
        return len(self.owner)

<strong>    def __del__(self): # del 함수를 반환할 때 사용하는 메소드
</strong>        print("This car has been deleted")

    def __eq__(self, other): # 객체들끼리 비교했을 때 사용하는 메소드
        return self.color == other.color

tesla = Tesla("Joon", "Yellow")
# print(tesla)
# del tesla

tesla1 = Tesla("Aain", "White")
print(tesla == tesla1)
</code></pre>

> <mark style="color:orange;">**`str()`**</mark><mark style="color:orange;">** **</mark><mark style="color:orange;">**과**</mark><mark style="color:orange;">** **</mark><mark style="color:orange;">**`repr()`**</mark><mark style="color:orange;">**의 차이**</mark>
>
> 둘은 엄연히 차이가 있습니다.
>
> * `__str__`은 서로 다른 자료형 간에 인터페이스를 제공하기 위해 존재합니다.
> * `__repr__`는 해당 객체를 인간이 이해할 수 있게 하기 위해 나타내는 표현입니다. 둘은 본질적으로 다릅니다.
>
> 우선순위를 따지자면 `__str__`가 더 높습니다. 그래서 `__repr__`를 작성하지 않으면 사용자의 편의를 제공하지 않기 때문에 데이터 객체간 정보가 출력되는 것이죠.
>
> [👉 \[Python\] \_\_str\_\_와 \_\_repr\_\_의 차이 살펴보기 - shoark7.github.io](https://shoark7.github.io/programming/python/difference-between-\_\_repr\_\_-vs-\_\_str\_\_)
