# Repartition 과 Coalesce

RDD를 생성하고 다양한 trasformation 연산을 수행하게 되면 파티션의 개수가 변하게 됩니다. 이런 경우 현재의 <mark style="color:orange;">**파티션 개수를 조정하는 연산**</mark>이 있습니다.

<table><thead><tr><th width="82"></th><th>Repartition</th><th>Coalesce</th></tr></thead><tbody><tr><td>특징</td><td>파티션의 갯수를 조정</td><td>파티션의 갯수를 조정</td></tr><tr><td>연산</td><td>파티션 수 증가, 감소</td><td>파티션 수 감</td></tr><tr><td>셔플</td><td>강제 수행</td><td>옵</td></tr></tbody></table>

## Repartition

```python
# 1
df = df.repartition(10, 'city') # 파티션 갯수, 컬럼 이름

# 2
df = df.repartition('city', 'region') # 컬럼 이름만
```

* 파티션의 수를 파라미터로 넣어 파티션의 개수를 조정하는 함수
* 해시 기반 파티셔닝, 넓은 종속성
* Repartition을 한다고 해서 모든 파티션의 데이터가 동일하지 않는다.
* 메모리 이슈나 Skewed 데이터가 있는 경우 사용한다.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### repartitionByRange()

```python
df.repartitionByRange(2, 'age') # 파티션 갯수, 컬럼 이름
```

* 데이터 값과 비슷한 것끼리 샘플링하는 함수

## Coalesce

* 파티션을 줄이는데 사용하는 함수
* repartiton에 반해 셔플링은 하지 않고 파션을 합친다.&#x20;

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

{% embed url="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.coalesce.html#pyspark.RDD.coalesce" %}
