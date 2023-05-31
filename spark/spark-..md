# Spark를 소개합니다.

## Introduce Spark

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption><p>Spark Component</p></figcaption></figure>

Spark는 **대량의 데이터(Batch Data)를 쪼개 동시에 처리**할 수 있는 빅데이터 처리 엔진입니다. 이전에는 Hadoop을 사용했으나 속도면에서 워낙 Spark가 빠르기 때문에 Spark를 많이 사용하게 되었습니다.

> 하둡(Hadoop)과 가장 큰 차이점으로는 디스크에서 읽고 처리하는 방식이 아닌 **메모리 안에서 데이터를 처리**한다는 점입니다.&#x20;

## Structure

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>Spark Structure</p></figcaption></figure>

위 구조를 자세히보면,&#x20;

1. Driver Program(Python)이 Cluster Manager에게 신호를 보냅니다.
2. Clutter Manager는 작업을 WorkerNode에게 분배를 합니다.
3. 그렇다면 실질적으로 Executor가 연산을 하고 다시 Driver Program에게 전 을합니다. ( 1 CPU : 1 Worker Node)

> Worker Node는 Cache를 공유하면서 작업의 속도를 높일 수 있어요.

## RDD

스파크에서 가장 중요한 역할을 하는 RDD입니다.

RDD는 **여러개 노드에 분산되어 있는 데이터셋**입니다. 그래서 탄력적 분산 데이터셋(Resilient  Distributed Dataset)이라고 합니다.&#x20;

RDD의 큰 특징으로 다음과 같습니다.

* **Lazy Evaluation** : 파이썬의 Generator 처럼 필요할 때마다 액션을 실행하는 녀석입니다.  액션을 실행하기 전까지는 연산을 하지 않아요. 그래서 게으른 연산이라고 합니다.
* **Immutablity** : 처리하는 도중에 데이터는 바뀌지가 않기 때문에 노드가 망가져도 다시 복원을 할 수 있습니다. 그래서 탄력적입니다.
* **abstract :** 분산 처리이기 때문에 데이터가 흩어져 있어도 하나의 파일 인 것처럼 사용합니다.

> **Spark Operations**
>
> 앞에 등장했었던 액션(Action)과 변환(Trasformation)이라는 단어가 익숙치 않을 것입니다. Spark에서는 위 두가지 연산을 잘 사용합니다.
>
> * **Transformation** : 바꾼다는 의미가 아니라 새로 RDD를 생성한다는 의미가 강합니다. 이 작업을 수행할 때마다 연산 기록이 남게 됩니다.&#x20;
> * **Action** : 실제로 메모리에 올려 연산을 수행하는 작업입니다.







