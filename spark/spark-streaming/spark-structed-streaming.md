# Spark Structed Streaming

지난 Spark Streaming(Prev)과는 다르게 Structed Streaming에서는 DataFrame을 기반으로 사용하기 때문에 DataFrame API를 사용할 수 있게 `Spark Session` 객체를 생성합니다.

이전 SQL과 다른점은 스트리밍 데이터 프레임을 사용하기 위해 [<mark style="color:orange;">**`.readStream`**</mark>](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.readStream.html?highlight=readstream#pyspark.sql.SparkSession.readStream) 을 통해 변환 후 format과 option을 설정해면 스트림 데이터를 가져올 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

lines = spark \ 
    .readStream \ 
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()
    

```

라인들을 `select()` 하게되면 라인별로 공백을 기준으로 `split` 을 하고 단어들을 하나하나 마다 다음 라인으로 바꾸는 `explode` 를 실행합니다. 그리고 모든 라인을 words `groupby` 합니다.

```python
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

words = lines.select(
    explode(
        split(lines.value, " ")
    ).alias("word")
)

# Action
wordCounts = words.groupBy("word").count()
```

`.writeStream` 은 스트리밍 데이터를 외부 저장소에 저장하기 위한 인터페이스입니다. `.outputMode`에는 complete나 append가 있는데 전체의 데이터를 저장할 것인지 하나하나 저장할 것인지를 의미합니다. 출력할 장소를 `.format` 을 통해 지정할 수 있습니다.

```python
query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```

![](<../../.gitbook/assets/Screenshot 2023-06-23 at 18.04.32 (2).png>)

