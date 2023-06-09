# functions :  함수 사용하기

pyspark의 sql은 다양한 함수들을 사용할 수 있어요.

* **`round(col, 소수점)`** :  소수점 반올림을 위한 함수
  * `format_number(col, 소수점)` : 소수점까지 표현을 위한 함수
* **`sum(col)`** : 합계를 구하는 함수
* **`explode(col)`** : **Transpose**와 같은 기능으로 col과 row를 치환할 수 있다.
* **`size(col or str)`** : 해당 배열이나 문자열의 길이를 구하는 함수

```python
df = spark.createDataFrame([
        Row(a=1,
            intlist=[1,2,3],
            mapfield={"a": "b"}
           )])

df.show()
df.select(functions.explode(df.intlist).alias("anInt")).show()
# output: [Row(anInt=1), Row(anInt=2), Row(anInt=3)]
```

<figure><img src="../../.gitbook/assets/image (6).png" alt="" width="375"><figcaption></figcaption></figure>

* **`split(str, pattern, limit=-1)`** : **문자열 데이터를 패턴에 적용시켜 분할** 하여 리스트로 만들 수 있다. 만약, 한번만 분할하고 싶으면 `limit=1` 로 설정하면 된다.

```python
# functions.split(str, pattern, limit=-1)
# Splits str around matches of the given pattern.
df = spark.createDataFrame([
        Row(word="hello world and pyspark")])
df.select(functions.split(df.word, ' ').alias("word")).show()
```

* **`udf(function)`** : 사용자 정의 함수를 만들어낼 수 있는 함수입니다.&#x20;

```python
def get_occupation_name(occupation_id:str) -> str:
    return occupation_dict.value[occupation_id]
    
occupation_lookup_udf = f.udf(get_occupation_name)
# lambda 함수를 바로 사용해도 됩니다.
```

* **`collect_set(col)`** : **중복된 원소를 제거한 상태**의 set 자료형으로 반환합니다. (`collect_list(col)`와 차이가 있다면, 중복 여부의 차이 있겠죠?)
* **`concat_ws(sep, cols)`** : 여러개의 데이터들을 sep(구분자) 단위로 하나의 문자열로 반환합니다.

<pre class="language-python"><code class="lang-python"><strong># ABCISSA|[ELSIE DEE, FURY,...]
</strong><strong>data = data.withColumn("connection", f.concat_ws(",", f.col("connection")))
</strong><strong># ABCISSA|ELSIE DEE,FURY, C...
</strong></code></pre>

* `year(col), month(col), dayofyear(col), dayofmonth(col)` : 날짜를 다루는 데 사용하는 함
