# Spark Streaming

Spark Streaming은 실시간으로 <mark style="color:orange;">**끊임없이 들어오는 데이터를 처리하기 위한 모듈**</mark>입니다. 이렇게 시간 대 별로 들어오는 데이터를 개발자가 Batch 단위로 합쳐 처리하거나 분석을 하게됩니다.  Spark Stream 데이터들은 기본적으로 Python WebSocket이나 Kafka, Kinesis와 같은 리소스를 통해 들어오게 됩니다.

스파크 streaming은 두가지 개념으로 쪼개 이해할 수 있습니다.

* Spark Streaming
* Spark Structured Streaming

## Spark Streaming based RDD

> 데이터가 들어오게되면 `flatMap` 을 통해 Batch 데이터 단위로 잘라 데이터를 처리하게 됩니다.

<figure><img src="../../.gitbook/assets/image (9).png" alt="" width="563"><figcaption></figcaption></figure>

실시간으로 스트림 데이터를 받아 DStream을 통해 데이터를 배치 단위로 쪼개 처리합니다. 그리고 나서 Spark Engine이 데이터를 분석하게 됩니다.&#x20;

### DStream

DStream(distretized stream)은 시간대 별로 도착한 데이터들의 모임을 의미합니다. 다양한 리소스를 통해서 DStream으로 데이터를 전달받을 수 있습니다.

#### 연산

DStream 연산은 RDD와 마찬가지로 두가지 연산을 제공합니다.

* Transformation : RDD와 유사하게 `Map` `FlatMap` 같은 함수를 사용할 수 있습니다.
* Output : 파일 시스템이나 데이터 저장소에 저장하거나 출력할 수 있는 결과 연산을 의미합니다. `print()` 나 `saveTextFile` 과 같은 연산이 있습니다.

이외에도 시간을 관리하거나 이전 데이터의 정보를 확인할 수 있는 Window 연산도 존재합니다.



## Spark Structured Streaming based DataFrame

> Spark에서 구조적 API(Dataframe, Dateset)를 제공하는 최적화된 모듈입니다.

Spark Structured Streaming은 스트리밍 처리에 필요한 최적화나 정확성을 지원합니다. 그리고 checkpiont를 설정할 수 있어 장애가 발생해도 다시 처리할 수 있습니다. 타임스탬프를 이용해 데이터 생성기준으로 처리를 진행합니다.



