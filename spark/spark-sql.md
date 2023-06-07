# Spark SQL

## Spark SQL

* **Dataframe**을 이용하여 Query하여 데이터를 처리할 수 있습니다.

<figure><img src="../.gitbook/assets/carbon-5.png" alt="" width="375"><figcaption></figcaption></figure>

1. **Hive Integration** : Hadoop에서 사용했던 Hive Query 툴을 Spark SQL에서 사용이 가능합니다.
2. **Standard Connectivity** : BI 툴에서 SparkSQL로 Query를 보낼 수 있습니다.
3. **Industry Trend** : 현재 RDD보다 Dataframe을 더 많이 사용하는 추세

> #### RDD보다 Dataframe을 더 선호하는 이유?
>
> DataFrame은 RDD에 반해 Column과 Row로 이루어진 구조화된 데이터로 사람들이 쉽게 데이터를 처리할 수 있기 때문입니다. RDD는 구조화가 되어있지 않고 Low-Level의 API를 제공하기 때문에 불편한 감이 있겠죠. 그러나 RDD는 쓰면 안된다는 것은 아닙니다. RDD는 주로 비 구조화된 데이터를 사용하거나 최적화나 스키마를 굳이 따지고 싶지 않다거나 함수형 프로그래밍을 사용하고 싶을 때 RDD를 사용합니다.&#x20;

#### DataFrame

* `Schema` 를 만들거나 JSON,CSV,Hive,Avro,PArquet, ORC등을 읽거나 작성할 수 있습니다.
* JDBC나 ODBC,  Tabluau 툴과 연결할 수 있습니다.



#### 참고

* [https://spidyweb.tistory.com/326](https://spidyweb.tistory.com/326)
