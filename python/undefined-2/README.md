# 파일 처리하기

### 파일 처리하기

파일을 처리할 때는 파일을 메모리에 할당을 한다음, 처리를 합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235844311-be8416ff-ff7d-46c1-9803-02135d18e05d.png" alt=""><figcaption></figcaption></figure>

만약에 파일을 메모리에 할당을 하고 `close`를 하지 않으면 사용하지 않은 데이터가 메모리에 계속 할당이 되는 상황이 발생합니다. 그래서 반드시 `close`를 해주어야 합니다.

> **📌 메모리 관리에 관해**
>
> 과거와 다르게 현재는 Modern Language를 사용합니다. 특히, 파이썬에는 **Garbage Collector**라는 것이 존재하는 데 이는 변수가 지정하지 않은 메모리가 존재할 경우 안쓰이면 삭제해버리는 청소꾼같은 역할을 합니다.

```python
file = open("README.txt", "r")  # 파일 명, 파일 모드
print(file.read())  # 파일 읽기
file.close()
```

이러한 문제를 해결하기위해 아래 방법도 이용합니다.

```python
with open("README.txt", "r") as file:
  print(file.read())

with open("README.txt", "w") as file:
  print(file.write("\n Yes!"))  # 4 : 4개의 스트링을 저장함, 문서를 초기화

with open("README.txt", "a") as file:
  print(file.write("\t No!"))  # append : 문서에 데이터를 추가함.
```

### CSV 파일 처리하기

`csv` 라이브러리를 사용하면 csv 파일을 쉽게 불러올 수 있습니다.

```python
# CSV (Comma seperate Values)

file = open("sample.csv", "r")
print(file.read())
file.close()

# using package
import csv

with open("sample.csv", "r") as data:
  data = csv.reader(data)
  for row in data:
    print(row)

import pandas as pd
# 분산 처리(Spark)보다 싱글노드에 가장 많이 사용

data = pd.read_csv("sample.csv")
print(data)

print(data['location'])
```

### JSON 파일 처리하기

> JSON은 **모든 언어들이 지원 가능하고 읽기 쉬운 format** 이지만, 읽고 쓰기엔 느린 포맷이므로 다른 압축 format을 많이 사용합니다.

Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷입니다.

```json
{"external_urls": {"spotify": "string"}, "genres": ["Prog rock", "Grunge"], "href": "string", "id": "string", "images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228", "height": 300, "width": 300}], "name": "string", "popularity": 0, "type": "drink", "uri": "string"}
```

```python
import json

with open("sample.json", mode='r') as f:
    # JSON 파일 불러오기 
    data = json.loads(f.read()) # f.read() vs json.loads() str vs dic
    print(data['type'])
    
    data['type'] = 'drink'

    # JSON 파일 수정하기
    with open("sample.json", mode="w") as w:
        w.write(json.dumps(data))
```

#### `pprint`

* 딕서너리 형식에 `pprint()` 메소드를 사용하면 JSON 형식 **읽기 쉽게(pretty)** 으로 출력합니다.

```python
from pprint import pprint
pprint(json_dic)
```

* [JSON placeholder](https://jsonplaceholder.typicode.com/)
* [Json.org](https://www.json.org/json-en.html)
