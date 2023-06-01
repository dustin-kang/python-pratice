# Spark 설치하기



## A. Docker 기반 Spark 설치하기

> 진행하기 앞서, [Docker.com](https://www.docker.com)에서 운영체제에 맞는 Docker를 설치합니다.

아래 코드와 같이 Docker를 통해 Local root와 Internal root를 연결시킵니다.

이미지를 다운받게 되면 중간에 링크가 등장하는데 링크를 통해 Jupyter에서 사용하시면 됩니다.

```docker
docker run -it --rm 8888:8888 -v /Users/Local:/home/jovyan/work jupyter/pyspark-notebook
```

### A-1. JuypterNotebook 안으로 들어가는 법

`ps` 를 통해 실행중인 프로세스를 확인한 다음, 컨테이너의 ID를 통해 들어가시면 됩니다.

```
docker ps 
docker exec -it {CONTAINER ID} /bin/bash
```

## B. DataBricks 커뮤니티 에디션을 통해 스파크 실행

[https://www.databricks.com](https://www.databricks.com) 사이트를 이용하여 웹을 통해 Note를 작성할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>



## &#x20;Pyspark 사용해보기

Juypter Notebook을 열게되면 Python 코드를 작성할 수 있는 문서를 만들 수 있습니다.

#### SparkContext

```python
import pyspark

sc = pyspark.SparkContext('local[*]')
```

파이썬 라이브러리로 `pyspark`를 불러옵니다.&#x20;

Pyspark 라이브러리에서 **`SparkContext`**라는 클래스를 사용할 수 있습니다. &#x20;



### pySpark 아키텍처 이해하기

SparkContext라는 클래스가 물리적으로 생성되는 과정을 알 필요 있습니다.&#x20;

<figure><img src="../.gitbook/assets/image (3) (1).png" alt="" width="563"><figcaption><p>Pyspark Dataflow</p></figcaption></figure>

<mark style="color:green;">**우선, Spark는 JVM 위에서 동작합니다.**</mark> Python Driver가 직접적으로 Spark Core에 접근할 방법은 없죠. 그렇기 때문에 Python Driver는 JVM을 통해서 Spark Core에 접근이 가능합니다.

그렇다면 위 PySpark가 실행되는 프로세스를 봅시다.

Python에서 PySpark를 실행하려면 Python이 Java의 Spark를 실행하기 위해 Py4j라는 프로그램이 필요로 합니다. Py4j를 통해 JVM을 실행시킬 수 있습니다. JVM을 통해 Spark Context를 생성할 수 있습니다. 그리고 Spark Context는 Worker로 PySpark를 구동시킬 수 있는 것입니다.&#x20;

**그렇다면 Cluster에 왜 Python Worker가 존재할까요?**

만약 우리가 Python Library가 필요로 할때, Spark Worker만으로는 Pandas나 Numpy와 같은 Python Library를 실행시킬 수 없습니다. 파이썬 라이브러리를 실행시키 위해 Python Worker가 필요한 것입니다. 그리고 이 Worker에게는 파이썬 Library가 반드시 설치되있어야 합니다.

### rdd 생성

```python
rdd = sc.parallelize(range(1000))
rdd.taskSample(False, 5) # 0~1000까지 데이터 중 5개를 추출합니다.
```

SparkContext에서 RDD를 생성할 수 있습니다. 기존의 데이터들을 `parallelize` 라는 메소드를 통해 RDD 객체로 만들어줍니다. 이전 페이지에서 나왔듯, RDD는 불변한 분배 객체이기 때문에 데이를 변경할 수 없습니다.



## 참고

* [https://surgach.tistory.com/105](https://surgach.tistory.com/105)
