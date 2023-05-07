# 파이썬 웹 요청하기

<img width="827" alt="image" src="https://user-images.githubusercontent.com/55238671/226222544-2f3eb7cc-42af-438b-a0e1-a87d50a75669.png">


### CRUD
| HTTP 메서드 | 설명 | 사용 예 |
| --- | --- | --- |
| GET | 데이터 조회 | 검색 및 접속 |
| POST | 데이터 생성 | 가입, 글 작성 |
| PUT | 데이터 수정 | 수정 |
| DELETE | 데이터 삭제 | 삭제 |

클라이언트(Client)는 웹상에서 요청을 하기위해 **`HTTP`(HyperText Transfer Protocol : 주고받기 위한 프로토콜) 메서드**를 사용해서 통신을 진행합니다.
클라이언트가 HTTP 메서드를 이용해 서버에게 요청하면 서버는 적절한 기능을 수행합니다. 
반드시 아래 Rule을 따라야 하는 것은 아닙니다. 정보를 삭제할 때 POST 메서드를 사용할 수 있어요. **하지만 대부분 REST한 방식을 따릅니다.**

```python
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)
```

위와 같이 `requests` 라이브러리를 설치해서 **GET 방식**으로 구글 사이트의 **HTML을 출력**할 수 있습니다. 
어떤 메서드를 사용할지는 서버의 구현에 따라 달라질 수 있는데 대부분의 웹 사이트에서는 POST 기능으로 삭제 수정 요청을 처리하기도 합니다.
**즉, 클라이언트는 서버가 구현한 기능에 맞게 적절한 요청을 보내야 합니다.**

# API 호출

## REST API

### REST
자원의 상태에 대해 주고 받는 개발 방식으로 자원을 어떤 방식으로 접근할지 구체적으로 명시하는 것입니다.
1. 자원(Resource) : URI를 이용하여 표현 _`/users`_
2. 행위(Verb) : HTTP 메서드를 이용하여 표현 _`GET`_
3. 표현(Representations)

이때, 아이디나 비밀번호와 같은 구체적인 정보는 페이로드(payload)에 담아서 보냅니다.

### API
- 클라이언트와 서버가 상호작용하기 위한 인터페이스 입니다.
- REST API : REST 아키텍처를 따르는 API
- REST API 호출 : REST 방식을 따르고 있는 서버에 요청을 보내 데이터를 가져오는 것을 말합니다.


## JSON

### JSON
- **데이터를 주고받는 데 사용**하는 경량의 데이터 형식입니다. 
- **키-값 쌍**으로 이루어진 데이터 객체를 저장하고 있습니다.
```json
{
    "id" : "Ariana",
    "password" : "202203",
    "age" : 30,
    "hooby" : ["sing", "programming"]
}
```

### JSON 인코딩 예시
파이썬 기본 자료형을 JSON 객체로 변환하는 작업을 말합니다. `json.dumps()` 메서드를 이용해 객체를 생성할 수 있습니다.
```python
import json

# 사전 자료형(딕셔너리) 데이터 선언
user = {
    "id" : "Ariana",
    "password" : "202203",
    "age" : 30,
    "hooby" : ["sing", "programming"]
}

# 인코딩
json_data = json.dumps(user, indent = 4) # indent : 띄어쓰기 4칸 들여쓰기 적용
print(json_data)

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file: 
    json.dump(user, file, indent = 4)
```

### JSON 디코딩 예시
위 인코딩과 반대로 JSON 객체를 파이썬의 자료형으로 변환하는 작업을 말합니다. `json.loads()` 메서드를 이용합니다.

```python
import json

# 디코딩
data = json.loads(json_data)
print(data)
```

- [JSON Placeholder](https://jsonplaceholder.typicode.com) : JSON 가상 목킹 사이트


## REST API 호출 실습

- 파이썬에 제공되는 서드파티 라이브러리로 API를 불러와 데이터르 추출하는 API입니다.

<img width="653" alt="image" src="https://user-images.githubusercontent.com/55238671/236669948-a9cc725b-6462-4c46-a132-9d13cc2b4146.png">


```python
import requests

target = "http://jsonplaceholder.typicode.com/users"
response = requests.get(url = target)

# 응답 데이터인 json 형식을 파이써 객체로 변환
data = response.json()

# 이름정보를 name_list라는 리스트에 담기
name_list = []
for user in data:
    name_list.append(user['name']) 
```
