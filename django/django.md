# Django 설치하기

## Python 환경 구성(pyenv)

파이썬의 다양한 버전을 관리하는 환경입니다.

* [Brew 사이트](https://brew.sh/index\_ko)

```bash
# pyenv 설치
brew update
brew install pyenv

# 파이썬 버전 설치
pyenv install -list
pyenv install 3.9.14 # uninstall은 삭제

pyenv versions
pyenv global 3.9.14 # 3.9.14 버전 글로벌 설정 
```

## 프로젝트 환경 구성

### Anaconda 가상환경 구성

* 라이브러리간 의존성 해결

```bash
conda --version # 버전 확인
conda update conda  # 업데이트

conda search python # 파이썬 리스트
conda install python=3.9.15 # 파이썬 버전 설치

conda create -n blog python=3.9.15 # 가상환경 생성
conda remove -n blog -all # 가상환경 삭제

# 이외
conda install <패키지명>
conda info --env # 가상환경리스트
conda activate # 활성화

```

### venv로 가상환경 구성

파이썬 2에서는 가상환경 라이브러리가 제공되지 않았기 때문에 `virtualenv`를 사용했었다.

그러나 파이썬3에서는 `venv`라이브러리를 기본적으로 제공하기 때문에 `virtualenv`를 사용하지 않아도 된다.

```bash
python -m venv <가상환경 이름>
```

### jpyenv의 가상환경 구성

```bash
brew install pyenv-virtualenv

# 파이썬 가상환경 생성
pyenv virtualenv <가상환경 버전> <가상환경 이름>
pyenv virtualenv <가상환경 이름>

# 파이썬 가상환경 삭제
pyenv uninstall <가상환경 이름>

# 가상환경 실행 및 비활성화
source activate <가상환경 이름>
deactivate <가상환경 이름>
```

***

## Docker

**도커를 사용하는 이유**

* 협업을 할 때, 모든 개발 환경이 다르기 때문에 **일치하는(consistent) 환경을 만들기 위해** 사용합니다.

**도커 실행 사이트**

* [https://www.docker.com](https://www.docker.com)
* [Docker Hub - 이미지 라이브러리 사이트](https://hub.docker.com)

### 사용하기

<figure><img src="https://user-images.githubusercontent.com/55238671/235630931-bcf10d14-7158-42bb-b624-8f1cd46f9687.png" alt=""><figcaption></figcaption></figure>

#### Dockerfile 만들기

```docker
# Image:Version, Docker hub에서 버전을 찾을 수 있습니다.
FROM python:3.11.3  

# 모든 로그를 stdout 이나 stderror로 보낸다는 뜻입니다. 나중에 차차...
ENV PYTHONUNBUFFERED 1 

ARG DEV=false 

# COPY : 로컬 환경에 있는 requirements.txt이나 폴더를  도커 환경의 /app/에 넣겠다는 뜻입니다.
COPY requirements.txt /app/ 
COPY requirements.dev.txt /app/ 
COPY app /app/ 

# WORKDIR : 도커 이미지 안 명령어를 시작할 때 시작할 위치를 설정합니다. WORKDIR 밑에 있는 RUN 명령어는 해당 위치에서 명령어가 시작합니다.
WORKDIR /app 
RUN pip install -r requirements.txt 

# AVG 인자를 오버라이딩 하여 true일 경우 dev(개발자 파일)을 실행하는 것을 말합니다.
RUN if [ $DEV = true ]; then pip install -r requirements.dev.txt; fi

# EXPOSE : 도커 안에 있는 포트를 로컬 환경의 포트와 소통하겠다는 의미입니다. 
EXPOSE 8000
```

#### Docker Compose 만들기

* Docker Compose : 여러개의 컨테이너를 관리합니다. 로컬 환경과 Docker 환경 사이에 포트나 파일 시스템을 연결시켜줍니다.
* `Docker build` : Docker 이미지를 만듭니다.
* `Docker up` : 이미지가 만들어진 상태에서 실행합니다.

```yml
version: '3.9' # 버전을 입력합니다.

services:
  app: # 연결할 서비스를 작성합니다. ex) app, database
    build: # context를 사용안하고 build만 사용해도 됩니다.
      context: .
      args:
        - DEV=true
    ports:
      -"8000:8000" # 로컬포트:Docker포트
    volumes:
      - ./app:/app # 로컬볼륨:도커볼륨
    command: >
      sh -c "python manage.py runserver 0.0.0.0:8000"
 # 도커 안에 명령을 넣어줄 수 있습니다.

```

#### 모든 환경 실행을 위해 Docker Compose 명령하기

* `docker ps` : 도커가 실행중인 상태인지 확인하는 명령어
* `docker compose build` : 도커 이미지를 만드는 명령어
* `docker image ls` : 도커 이미지 확인하는 명령어
* `docker compose up` : 만들어진 이미지를 찾아 명령어를 실행
* `docker exec -it [CONTAINER ID] /bin/bash` : 도커 안으로 들어가서 확인이 가능합니다. `ps aux`로 명령어가 실행 중인지 확인 가능합니다.
* `Ctrl + C` 로 종료할 수 있습니다.

### 참고자료

* [가상 환경에 대한 이해: pyenv, virtualenv, anaconda - ooeunz 블로그](https://ooeunz.tistory.com/50)
* [아니콘다 파이썬 환경 변경하기 - Technical Support](https://technical-support.tistory.com/85)
* [아니콘다 사이트](https://www.anaconda.com/products/distribution)
