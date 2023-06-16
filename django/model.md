# Model 설계하기

## Django Model

#### Database

웹 개발을 할때 고민해야될 선택 중 하나는 어떤 데이터베이스를 사용하느냐입니다.

데이터베이스 두가지 `NOSQL`과 `SQL`로 나뉘게 되는데요. 이 둘은 각자 장단점이 있으니 잘 판단해서 선택하는 게 좋습니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/236680597-692d9c68-5ce8-461f-9043-ce5cb77f288f.png" alt=""><figcaption></figcaption></figure>

**SQL**

* 중복을 줄이기 위해 '관계'라는 것을 이용합니다. 그래서 **무결성이 보장**되는 데이터베이스 입니다.
* SQL 데이터베이스는 일반적으로 수직적인 확장을 지원합니다. 확장을 위해 CPU 업그레이드가 필요하죠. _**(Scailing Up)**_

> 데이터 변경이 잦고 데이터베이스의 변경이 많이 없을 때 용이합니다.

**NoSQL**

* 스키마가 없고 애플리케이션이 필요한 형식대로 저장하기 때문에 데이터 읽어오는 **속도가 빨라집니다.**
* NoSQL 데이터베이스는 수평적인 확장도 지원합니다. 주로 JSON을 이용하기 때문에 하드웨어를 분산해서 처리가 가능하고 모든 읽기 쓰기 요청 처리가 가능합니다. _**(Scailing Out)**_

> 막대한 양의 데이터를 다루거나 정확한 데이터 구조를 알 수 없을 때 용이합니다.

**참고**

* [👉 NoSQL과 SQL의 차이 - gyoogle](https://gyoogle.dev/blog/computer-science/data-base/SQL%20&%20NOSQL.html)
* [👉 NoSQL과 SQL의 차이 - MongoDB 관점](https://www.mongodb.com/nosql-explained/nosql-vs-sql)

### 👨‍💻 Django에서는 데이터베이스를 어떻게 사용하는가?

<figure><img src="https://user-images.githubusercontent.com/55238671/236682013-b4074d47-2d8d-4230-a17a-25df9dd094e3.png" alt=""><figcaption></figcaption></figure>

* [👉 Database configuration](https://docs.djangoproject.com/en/4.2/ref/settings/#databases)
* [👉 Sqlite DB Browser](https://sqlitebrowser.org/dl/)

#### Model

> 데이터의 대한 확실한 정보를 저장하는 곳을 말합니다. 일반적으로 데이터베이스 테이블과 연결되어 있습니다.

* Django는 자동적으로 데이터베이스 CRUD를 지원합니다. (`models.py`에 클래스를 작성하면 자동으로 SQL로 바꿔줍니다.)

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

* [📌 장고모델 만들기](https://docs.djangoproject.com/en/4.2/intro/tutorial02/#creating-models)

#### 명령어 관리하기

<figure><img src="https://user-images.githubusercontent.com/55238671/236681719-3800a46b-81a3-4694-b114-d5227ab45ed8.png" alt=""><figcaption></figcaption></figure>

```sh
# 장고 한테 모델을 바꾸거나 새로 만들겠다는 내용의 파일을 만들어줍니다.
python manage.py makemigrations

# 만들어낸 파일과 데이터베이스 내 장고테이블과 비교해 적용이 됬는지 확인합니다. 이후 새로 데이터베이스 테이블을 만들어냅니다.
python manage.py migrate

# 장고 쉘을 통해서 데이터를 확인할 수 있습니다.
python manage.py shell
# from app.models import Choice
# Choice.objects.all() # ORM 작성
```

## Django Select Query

#### GET vs Filter

| get                      | filter                      |
| ------------------------ | --------------------------- |
| 객체(Object) 하나만 반환        | 객체(Object) 여러개를 반환 (리스트)    |
| 2 이상, None을 반환하면 에러 발생   | None이면 빈 값 출력               |
| `User.objects.get(id=1)` | `User.objects.filter(id=1)` |

#### Field Lookup

> 조건문을 사용할 때 쓰는 명령어입니다. `field__lookuptype=value` (field는 column과 동일합니다.)

* **lookuptype**
  * lte(<=)
  * iexact(Ignore Like)
  * contains(LIKE)
  * in(IN)
  * contains

> [👉 `lookuptype` 예제](https://docs.djangoproject.com/en/4.2/topics/db/queries/#field-lookups)

* JOIN : `TableA.objects.filter(tableB__fieldB='field_name')`
* Complex lookup, q : 복합체 Lookup (`django.db.models.Q`)
  * `Q` Loop Up을 모두 사용하고 일반적인 Look Up을 사용해야 합니다.

## Schema `UPDATE`

> 모델을 `UPDATE` 할때도 migrations 명령어를 이용합니다.

**주의사항**

1. 처음 컬럼을 `add` 할 때, 존재하는 값들이 없기 때문에 **`default`를 설정**해야합니다. (또는 `blank=True` 옵션을 넣어 빈공간(값)이 있어도 상관 없다는 걸 설정해야 합니다.)
2. 컬럼을 `remove`할 때, 코드에서 referring 하는 것들을 확실히 해야합니다.
3. 테이블을 새로 바꿨을 때, 잘못된 테이블은 반드시 ROLLBACK을 해야합니다.

```sh
# 3번 처럼 테이블을 잘못 바꿨을 때, migrate <app> <ROLLBACK할 마이그레이션 파일>을 입력해야 이전의 상태로 돌아갑니다.
python manage.py migrate apps 0001_initial
```

#### Validator

> 장고에서 **컬럼을 관리**할 때 사용하는 모듈입니다.

![image](https://user-images.githubusercontent.com/55238671/236685628-0682c3d3-5e98-4a5e-a669-08d22baff325.png)

[👉 validator](https://docs.djangoproject.com/en/4.2/ref/validators/)

#### UPDATE RECORD

```python
from apps.models import Question
q = Question.objects.get(pk=1)
q
# <Question: What's up?>
q.question_text = "How are you?" #UPDATE
q.save() # 데이터베이스의 저장
q
```

#### DELETE RECORD

```python
from django.utils import timezone
now = timezone.now()
q = Question(question_text="how old are you?", pub_date=now)
q.save()
Question.objects.all()

Question.objects.get(pk=2) # 2번째 데이터를 읽어 인스턴스로 만듬
q.delete() #DELETE
Question.objects.all()
```

## Admin page

> 장고에서 자동적으로 구현된 관리자용 웹페이지

#### Superuser 만들기

```sh
# superuser 만들기
python manage.py createsuperuser

## Username과 Email, Password를 입력합니다.
```

#### 관리자 페이지에 모델 등록

```python
from django,contrib import admin
from .models import Question
 
admin.site.register(Question)
```
