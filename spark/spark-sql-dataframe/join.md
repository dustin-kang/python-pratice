# Join

오늘은 Spark의 다양한 **Join 방법**에 대해 알아보도록 하겠습니다.

## Join 사용하기

`Join` 의 기본적인 형태는 아래 코드와 같으며 "how"에는 아래와 같은 방법들을 기재할 수 있습니다.

* `inner` : 교집합
* `fullouter` : Join을 하되 두 테이플의 null 값도 가져옴
* `left` :  Join을 하되 왼쪽(left) 테이블에 있는 데이터들을 기준으로 가져옴
* `leftsemi` : Join을 하되 양쪽 테이블에만 있는 데이터들 중 왼쪽 테이블만 가져옴
* `leftanti` : Join을 하되 왼쪽(left) **테이블에만** 있는 데이터들 중 왼쪽 테이블만 가져옴

```python
df_1.join(df_2, df_1.id == df_2.id, "how")
```

위 코드는 natural Join이 가능하며 `()&()` 연산자를 붙여 Multiple Join이 가능합니다. 추가로, `.filter()` 나 `.where()` 등 붙여 사용할 수 있습니다.&#x20;

또한 직접 `.createOrReplaceTempView("테이블명")` 을 지정하여 쿼리를 보낼 수 있습니다.



## Join 전략

Spark에서 Join을 수행하는 방법으로 두가지가 있습니다.

* 큰 테이블과 작은 테이블 조인(상대적)
* 큰 테이블과 큰 테이블 조인

### Broadcast Join

두 테이블 중 **작은 테이블**을 복사(공유)하여 **큰 테이블의 일부**와 Join 하는 방법이다.

```
import functions.broadcast
df = bigdf.join(broadcast(smalldf))
```

### Shuffle Hash Join

Shuffle Hash Join은 Map 단계와 Reduce 단계로 나뉘는 Map Reduce 기반 Join 방식입니다.

* Map : Join 칼럼을 기준으로 데이터프레임을 매핑합니다.
* Reduce : 데이터프레임을 Shuffle하여 같은 Join Key끼리 Join을 수행합니다.
* sql.join.perferSortMergeJoin을 False 로 설정해야합니다.

### Sort Merge Join

모든 Worker Node간에 All-to-all Communication을 하는 방식입니다.

1. 우선 두 테이블의 파티션을 정렬합니다.
2. 정렬된 데이터를 병합하면서 같은 Key끼리 Join합니다.

Shuffle Hash Join과 비교하여 클러스터 내 데이터 이동이 적은 경향이 있습니다.

> 이상적인 성능을 발휘하기 위해 파티션들은 최대한 같은 곳에 있어야 하며 클러스터에 균등하게 분배되어야 합다. 그렇지 않으면 노드에 부하되고 연산 속도느려집니다.&#x20;



#### 참고

* [https://dhkdn9192.github.io/apache-spark/spark-join-strategy/](https://dhkdn9192.github.io/apache-spark/spark-join-strategy/)

{% embed url="https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.join.html?highlight=join#pyspark.sql.DataFrame.join" %}
