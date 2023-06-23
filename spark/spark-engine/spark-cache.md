# Spark Cache

## Spark Cache

Spark는 재사용을 위해 다양한 옵션을 제공합니다. 재사용을 하게되면 데이터를 좀 더 빠르게 처리할 수 있고 효율적으로 처리할 수 있기 때문니다. 재사용을 통해 아래와 같은 성능을 향상시킬 수 있습니다.

* 반복적인 계산
* 여러번 액션 호출
* 오버헤드 감

이전 Spark의 구조를 소개했을 때 그림입니다. 캐시들은 각 WorkerNode 내 Executor에 <mark style="color:orange;">**설정된 메모리 만큼 파티션을 캐싱하는 것**</mark>이 가능합니다. 즉, 메모리 맞게 캐시에 Partition을 담아 사용할 수 있는 것이죠. 만약에 데이터가 메모리에 충분하지 않으면 Disk를 활용할 수 있습니다.

<figure><img src="../../.gitbook/assets/image (13) (1).png" alt="" width="340"><figcaption></figcaption></figure>

```python
dfCaced = spark.read.format("parquet").load("./data_parquet").cache()

dfCached.count()
dfCached.getStorageLvel
```

### Cache()와 persist()의 차이

두 함수들은 비슷한 역할을 하지만 <mark style="color:orange;">**`persist()`**</mark><mark style="color:orange;">** **</mark><mark style="color:orange;">**는 Storage Level을 파라미터로 받아 저장 공간을 정할 수 있습니다**</mark>. 여기서 Cache()는 모든 메모리에 RDD를 저장할 수 있습니다. 병렬작업을 효율적으로 사용할 수 있죠. 그리고 `persist()` 는 다양한 장소에서 저장을 할 수 있어요. 반복적인 연산을 피하기위해 Spark에 데이터 영속화(persist)를 요청할 수 있습니다.

#### Spark에서 Persist가 필요한 이유

다양한 장소에 저장할 수 있다는 말은 데이터를 스캔하는 반복성과 메모리 소비를 줄일 수 있는 다른 방법이 있다는 말이에요. 그래서 persist가 필요한 이유입니다. 그렇다면 이제 Storage Level에 따라 공간이 다르다고 앞서 말했는데요. 이에 대해 자세히 알아보도록 하겠습니다.

### Storage Level

<table><thead><tr><th width="270">레벨</th><th>공간 사용도</th><th>CPU 사용 시간</th><th>메모리 저장 여부</th><th>디스크 저장 여부</th></tr></thead><tbody><tr><td>MEMORY_ONLY</td><td>높음</td><td>낮음</td><td>Y</td><td>N</td></tr><tr><td>MEMORY_ONLY_SER</td><td>낮음</td><td>낮음</td><td>Y</td><td>N</td></tr><tr><td>MEMORY_AND_DISK</td><td>높음</td><td>중간</td><td>일부</td><td>일부</td></tr><tr><td>MEMORY_AND_DISK_SER</td><td>낮음</td><td>높음</td><td>일부</td><td>일부</td></tr></tbody></table>

`~SER` 로 적혀있는 것은 메모리를 직렬화된 상태로 저장하게 되는 것입니다. 그리고 `_DISK` 는 메모리에 넣기에 데이터가 너무 많아 디스크에 저장하는 것을 말합니다.

### Uncaching

캐싱의 반대 역할로 `unpersist()` 를 사용하면 됩니다.



#### 참고

* [https://jaemunbro.medium.com/apache-spark-rdd-재사용을-위한-영속화-persist-cache-checkpoint-12c121dac8b6](https://jaemunbro.medium.com/apache-spark-rdd-%EC%9E%AC%EC%82%AC%EC%9A%A9%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%98%81%EC%86%8D%ED%99%94-persist-cache-checkpoint-12c121dac8b6)
* [https://deviscreen.tistory.com/94](https://deviscreen.tistory.com/94)

{% embed url="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.persist.html#pyspark.RDD.persist" %}





