# WordCount 예제

Spark 소개 페이지에서 Docker를 Run 할때의 코드에서 환경변수(`-e`)를 추가하여 Run 합니다.

Spark Streaming이 클라이언트 어플리케이션이기 때문에 데이터를 받는 소켓서버가 필요하므로 netcat를 설치하고 netcat 서버를 설치합니다.

```bash
docker run -it --rm -p 8888:8888 \
    -v /Local:/home/jovyan/work \
    --user root \
    -e NB_GID=100 \
    -e GRANT_SUDO=yes \
    -e GRANT_SUDO=yes jupyter/pyspark-notebook

# 도커 안으로 들어갑니다.
docker exex -it {container_id} /bin/bash  
# 컨테이너 내 앱들을 업데이트 합니다. 
apt update
# 컨테이너 내 netcat이라는 소켓 서버를 설치합니다.
apt-get install netcat

# netcat 서버
nc -lk 9999


```

### 입력된 데이터 전송 받기

자 이제 Dokcer 단에 Jupyter Notebook을 여시고 해당 코드를 입력해줍니다.

```python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamimgContext(sc, 10)
```

* `SparkContext` App Name 이전에 `local[2]`로 코어를 2로 설정한 이유는 데이터를 전달하고 받는 행위까지 하기 위해 설정했습니다.
* **`pyspark.streaming`**<mark style="color:orange;">**`.StreamingContext`**</mark>는 Spark Streaming을 사용하기 위한 객체이며 파라미터로 SparkContext 객체와 입력된 데이터를 Batch 데이터로 분할하기 위한 인터벌 시간 의미합니다.

```python
lines = ssc.socketTextStream("127.0.0.1", 9999) # localhost:9999
```

* <mark style="color:orange;">**`scoketTextStream`**</mark>은 TCP 소켓을 사용하여 입력된 데이터를 받을 DStream을 만듭니다. 데이터를 받기 위해 연결할 Hostname("127.0.0.1")과 포트번호(9999)를 입력하시면 됩니다.
  * 만약 소켓이 아닌 Kafka와 같은 리소스를 사용하려고 하면 다른 Framework 공식문서를 참조하시면 됩니다.
  * 받은 데이터는 `\n` 을 기준으로 라인별로 주어집니다.

```python
# 해당 라인을 공백을 기준으로 단어별로 나눕니다.
words = lines.flatMap(lambda line: line.split(" ")) 
# 해당 단어들을 (word, 1) 쌍으로 만듭니다. 그리고 단어별로 갯수를 받습니다.
pairs = words.map(lambda word : (word, 1))
wordCOunts = pairs.reduceByKey(lambda x, y : x + y)
```

데이터를 가공하는 작업입니다.

```python
wordCounts.pprint()
```

DStream에서 생성된 각 RDD 요소들을 출력합니다.

```python
ssc.start() # 스트림 서버를 실행합니다.
ssc.awaitTermination() # 쿼리의 종료를 기다립니다.
```

![](<../../.gitbook/assets/Screenshot 2023-06-23 at 17.24.12.png>)

&#x20;위 그림을 보게되면 terminal에 line 문자열을 입력하면 알아서 연산을 한 상태로 출력하게 됩니다.

10초마다 인터벌을 보이는 것도 확인할 수 있습니다.

{% embed url="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.streaming.StreamingContext.html?highlight=streamingcontext#pyspark.streaming.StreamingContext" %}
