# 패키징, 압축하기

### 파일 압축 라이브러리 zip

```python
import zipfile

# 파일 압축
comp_file = zipfile.Zipfile('comp.zip', 'w')
comp_file.write('readme1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('readme2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# 파일 압축 풀기
zip_obj = zipfile.ZipFile('comp.zip','r')
zip_obj.extractall('extract_directory')
```

* `zipfile.Zipfile('압축파일이름','w')` : `w`는 압축, `r`는 풀기로 압축을 할 수 있다.

#### `shitil`를 사용하여 간결하게 압축하기

```python
import shutil

dir = "/zip/" # 압축할 프로젝트 경로
output = "zips"

# 압축
shutil.make_archive(output, 'zip', dir)

# 압축 풀기
shutil.unpack_archive(f"{output}.zip", 'extracted_dir', "zip")
```

### pickle

리스트나 딕셔너리와 같은 자료구조나 객체를 파일로 저장할 수 있는 라이브러리입니다.

```python
a = {'a' : 1}
b = ['b']
c = {1, 2, 3}

# 모든 데이터 자료구조를 한번에 파일화 할 수 있습니다.
with open('combine.pickle', 'wb') as f:
    pickle(a, f)
    pickle(b, f)
    pickle(c, f)

with open('combine.pickle', 'rb') as f:
    x = pickle(a, f)
    y = pickle(b, f)
    z = pickle(c, f)

print((x,y,z))
```

### [Poetry](https://python-poetry.org/docs/)

* 파이썬 패키징 도구 (Python 3.7+)

#### 사용법

* `poetry new <패키지 명>` : 새로운 파이썬 프로젝트 패키지를 생성합니다.
* `pyproject.toml` : 패키지의 가장 중요한 정보를 담고 있는 녀석입니다.

```sh
poetry shell
```

#### Library version dependencies

```sh
[tool.poetry.dependencies]
# 방법 1
pendulum = "^2.1"

# 방법 2
poetry add pendulum

# 설치 후 poetry.lock 파일이 만들어집니다.
poetry install
```

#### 패키지 CLI

```python
# kor이라는 명령어를 썼을 때 `package.submodule:fuction`이 실행이 됩니다.
kor = "kors.main:cli"
```

#### 테스트 케이스

```python
from kors.main import cli

def test_korean_cli(capsys):
    cli()
    captured = capsys.redouterr() # capsys를 사용해서 캡쳐
    result = captured.out
    assert "pykorean" in result

# $ poetry run pytest
```

#### 패키징

```sh
poetry build

poetry publish

# 하단의 경우는 private repo의 경우를 말합니다.
poetry publish -r my-repository
```

```sh
poetry config py-pi-token.pypi <API_TOKEN>

poetry build

poetry publish
```

**private repo**

[https://pypi.org/account/register/](https://pypi.org/account/register/) 에서 토큰을 생성합니다.

```sh
# PRIVATE REPO 생성
poetry source add --secondary <REPO_NAME> <REPO_LOCATE>
# PRIVATE REPO CREDENTIAL 생성
poetry config <REPO_NAME> <USERNAME> <PASSWORD>
#
poetry config certificates. <REPO_NAME>.cert false
# PRIVATE REPO에 패키지 생성
poetry add --source <REPO_NAME> <PACKAGE>

poetry build

poetry publish --repository <REPO_NAME>
```
