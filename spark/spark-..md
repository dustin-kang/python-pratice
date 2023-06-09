# Spark를 소개합니다.

## Introduce Spark

<figure><img src="../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption><p>Spark Component</p></figcaption></figure>

Spark는 **대량의 데이터(Batch Data)를 쪼개 동시에 처리**할 수 있는 빅데이터 처리 엔진입니다. 이전에는 Hadoop을 사용했으나 속도면에서 워낙 Spark가 빠르기 때문에 Spark를 많이 사용하게 되었습니다.

> 하둡(Hadoop)과 가장 큰 차이점으로는 디스크에서 읽고 처리하는 방식이 아닌 **메모리 안에서 데이터를 처리**한다는 점입니다.&#x20;

## Structure

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p>Spark Structure</p></figcaption></figure>

위 구조를 자세히보면,&#x20;

1. Driver Program(Python)이 Cluster Manager에게 신호를 보냅니다.
2. Clutter Manager는 작업을 WorkerNode에게 분배를 합니다.
3. 그렇다면 실질적으로 Executor가 연산을 하고 다시 Driver Program에게 전 을합니다. ( 1 CPU : 1 Worker Node)

> Worker Node는 Cache를 공유하면서 작업의 속도를 높일 수 있어요.

## PySpark 설치하기&#x20;

### A. Docker 기반 Spark 설치하기

> 진행하기 앞서, [Docker.com](https://www.docker.com)에서 운영체제에 맞는 Docker를 설치합니다.

아래 코드와 같이 Docker를 통해 Local root와 Internal root를 연결시킵니다.

이미지를 다운받게 되면 중간에 링크가 등장하는데 링크를 통해 Jupyter에서 사용하시면 됩니다.

```docker
docker run -it --rm 8888:8888 -v /Users/Local:/home/jovyan/work jupyter/pyspark-notebook
```

#### A-1. JuypterNotebook 안으로 들어가는 법

`ps` 를 통해 실행중인 프로세스를 확인한 다음, 컨테이너의 ID를 통해 들어가시면 됩니다.

```
docker ps 
docker exec -it {CONTAINER ID} /bin/bash
```

#### A-2. Local <-> Docker 파일 복사하는 법

* Local -> Docker

```
docker cp {local pwd}/. {CONTAINER ID}:/home/jovyan/work
```

* Docker -> Local

```
docker cp {CONTAINER ID}:/home/jovyan/work {local pwd}
```

### B. DataBricks 커뮤니티 에디션을 통해 스파크 실행

[https://www.databricks.com](https://www.databricks.com) 사이트를 이용하여 웹을 통해 Note를 작성할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>









