# Shared Variable

Spark에서 사용되는 공유변수(Shared Variable)에는 두가지 유형이 존재합니다.&#x20;

### [**Broadcast Variables**](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.Broadcast.html#pyspark.Broadcast)

* &#x20;**큰 규모의 데이터를 효율적으로 제공할 때 사용하기 위해** 사용하는 **읽기 전용 변수**입니다. 이는 효율성을 위해 Driver에 재전송 할 필요 없이 모든 Worker 단에서 Task가 공유받으면서 사용할 수 있는 변수를 의미합니다.
* 머신러닝 알고리즘 처럼 큰 사이즈의 벡터가 Worker 노드에 필요하다면 Broadcast Variable 를 사용하는 게 좋습니다.

<figure><img src="../../.gitbook/assets/image (10) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

```python
meta = {
    "1100": "engineer",
    "2030": "developer",
    "3801": "painter",
    "3021": "chemistry teacher",
    "9382": "priest"
}
occupation_dict = spark.sparkContext.broadcast(meta) # dictonary loading
print(occupation_dict.value)
# {'1100': 'engineer', '2030': 'developer', '3801': 'painter', '3021': 'chemistry teacher', '9382': 'priest'}
```

> 만약, BroadCast Variable을 Broadcast Join에 사용한다면 데이터가 상대적으로 작아야 합니다.

### [Accumulators](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.accumulator.html?highlight=accumulator#pyspark.SparkContext.accumulator)

* <mark style="color:orange;">**데이터들의 누적 합계를 집계할 때 사용**</mark>하는 공유 변수입니다.
* worker Node 별로 공유되어 Counter를 구현해 집계를 진행한 다음,  driver에서 값을 접근하여 결과 제공합니다. (driver에서만 값을 참조할 수 있습니다.)&#x20;

```python
acc = sc.accumlator(0)
rdd = sc.parallelize([1,2,3,4,5])
rdd.foreach(lambda x : acc.add(1)) # .add 를 사용하거나 += 연산자를 사용합니다.
print(acc.value)

```

#### 참고

* [https://mallikarjuna\_g.gitbooks.io/spark/content/spark-accumulators.html](https://mallikarjuna\_g.gitbooks.io/spark/content/spark-accumulators.html)
* [https://wooono.tistory.com/55](https://wooono.tistory.com/55)
* [https://dhkdn9192.github.io/apache-spark/spark-join-strategy/](https://dhkdn9192.github.io/apache-spark/spark-join-strategy/)
