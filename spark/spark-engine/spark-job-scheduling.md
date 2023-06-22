# Spark Job Scheduling

Spark 내 Job Scheduling 방식에는 두가지로 나뉘어 질 수 있습니다.

## Schedule Across Applications

이 방법는 하나의 Cluster가 여러 Application을 실행하기 위해 Spark가 Job Scheduling 하는 방법입니다.  이 방법에는 사용자에게 Task를 할당하는 방법이 또 두가지가 있습니다.

#### 정적 할당 (Static Allocation)

하나의 Cluster가 여러 Application을 실행하기 위해, 처음 사용자에게 Cluster가 가지고 있는 제한된 **최대 자원**을 할당하고 자원을 갖고있는 <mark style="color:orange;">**애플리케이션이 끝날 때 까지 기다리고 그 다음에 또다 애플리케이션이 실행되**</mark> 구조로 처리가 됩니다.

#### 동적 할당 (Dynamic Allocation)

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

Worker Node에 따라 Application이 점유하는 자원을 동적으로 조정하는 방식입니다. <mark style="color:orange;">**만약 애플리케이션이 사용하지 않은 자원이라면, 그만큼, 클러스터에게 반환을 하고 또, 그 만큼 필요하다면 그만큼 다시 요청하는 방식**</mark>입니다. 이렇게 보면 정적보다 동적 할당이 자원을 공유하는 데 더 유용하다고 볼 수 있죠.

## Schedule Within Application

```python
spark.scheduler.mode = FAIR # FIFO
sparkSession.config("spark.scheduler.mode","FAIR")
```

이 방법은 아까와는 다르게 하나의 어플리케이션 안에 여러 개의 job(Action)이 존재할 때 사용하는 Job Scheduling 방식입니다. 이 옵션에 대해 `FIFO` 아니면 `FAIR` 로 설정할 수 있습니다.

### Fair Scheduling Pool

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

default로는 FIFO로 되어있으나 하나의 Job에서 실행해야할 Task가 너무 많을 때, 대기시간 또한 길어지게 됩니다. 이러한 문제를 해결하기 위해 Spark에서 <mark style="color:orange;">**Fair Scheduling**</mark>이라는 기능을 제공합니다. 양쪽 그림을 비교해보면, **여러 Job을 분배하여 실행이 가능**하게 됩니다. Application의 실행시간도 줄이고 처리량도 올리고 여러개의 Pool를 구성하기 때문에 우선순위도 정할 수 있습니다.

```python
sc.setLocalProperty("Spark.scheduler.pool", "production")
```

{% code title="conf 템플릿에 Pool 설정" %}
```xml
<?xml version="1.0"?>
<allocations>
  <pool name="production">
    <schedulingMode>FAIR</schedulingMode> <? 모드 ?>
    <weight>1</weight> <? 리소스 점유율 제어 xn ?>
    <minShare>2</minShare> <? 각 pool의 최소 CPU 코어수  ?>
  </pool>
  <pool name="test">
    <schedulingMode>FIFO</schedulingMode>
    <weight>2</weight>
    <minShare>3</minShare>
  </pool>
</allocations>
```
{% endcode %}

{% code title="pool 속성 파일 저장" %}
```python
# scheduler file at local
conf.set("spark.scheduler.allocation.file", "file:///path/to/file")
# scheduler file at hdfs
conf.set("spark.scheduler.allocation.file", "hdfs:///path/to/file")
```
{% endcode %}

#### 참고

* [https://velog.io/@anjinwoong/Spark-Spark-FAIR-스케줄링에-대하여](https://velog.io/@anjinwoong/Spark-Spark-FAIR-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)







##
