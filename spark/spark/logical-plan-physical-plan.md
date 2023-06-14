# Logical Plan, Physical Plan

이번 글에서 실제 <mark style="color:orange;">**스파크 코드를 작성하면 실제 Spark가 어떻게 동작하는지**</mark>에 대해 알아보도록 하겠습니다.

실제로 Query를 작성한 후 [`df.explain(mode='extended')` ](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-explain.html)를 입력하면 확인할 수 있습니다. 이 코드를 통해 각 단계마다 어떤 플랜이 세워져 있는지 확인 가능합니다.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p><a href="https://www.databricks.com/glossary/catalyst-optimizer">https://www.databricks.com/glossary/catalyst-optimizer</a></p></figcaption></figure>

## Logical Plan

아직 Executor가 어떻게 실행할지를 고려하지 않고 <mark style="color:orange;">**논리적인 부분에서만 Transformation을 지정하는 단계**</mark>입니다.

#### 1. Unresolved Logical Plan (Parsed Logical Plan)

해당 테이블이나 컬럼 명이 유효한지 확인하는 단계입니다.

#### 2. Analyzer

실제로 컬럼과 테이블을 검증하는 단계입니다. 테이블의 저장소와 카탈로그를 통해 체크합니다.

대부분 TypeError 관련 문제들이 이 단게에서 발생합니다.

> Catalog : 데이터 구조나 스키마와 같은 메타 데이터(Meta data)들을 보관하는 저장소 입니다.

#### 3. Logical Plan (Analyzed Logical Plan)

데이터 구조나 스키마등에 대한 문제가 있는지 확인하는 단계입니다. 이후 계획 최적화를 위해 Catalyst Optimizer에게넘깁니다.

#### 4. Optimized Logical Plan

성능을 추정하는 단계입니다.

* 한 단계에서 작업들을 모두 수행하거나 계산할 수 있는지 확인합니다.
* 여러 개의 멀티 조인의 경우 어떤 작업을 먼저 두는게 가장 빠른지 순서를 정합니다.
* filter를 적용할 수 있는 지 체크합니다.

## Physical Plan

실제로 Logical Plan이 <mark style="color:orange;">**어떻게 실행되는지 물리적 실행 계획을 생성**</mark>하는 단계입니다.

#### 1. Physical Plans

테이블의 크기나 파티션의 수에 따라 물리적 속성을 고려하여 여러가지 플랜을 만들어 비교 가장 효율적인 플랜을 선택합니다.&#x20;

어떤 모델이 가장 빠르고 효율적인지 선택합니다.

플랜을 확인하면서, 불필요한 Exchange(셔플)이 많이 발생하지는 않았는지 또는 어떤 조인을 사용하고 있는지 확인합니다.

#### 2. Codegen

&#x20;위 작업이 완료되면 Tungsten 실행 엔진에 의해 <mark style="color:orange;">**RDD(DAG) 형태**</mark>로 컴파일 됩니다. &#x20;

## Adaptive Plan

런타임에서 전체 테스크나 스테이지를 제거할 수 있는 코드를 생성해 추가적인 최적화를 수행합니다.&#x20;



#### 참고

* [https://pizzathief.oopy.io/spark-logical-and-physical-plan](https://pizzathief.oopy.io/spark-logical-and-physical-plan)
