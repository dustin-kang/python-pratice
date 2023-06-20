# Spark Memory Management

## 메모리 할당

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Spark 내 메모리를 할당하는 방법에는 두가지로 나뉩니다.

### Memory Inside of JVM

```python
spark.memory.fraction=0.6 # Execution
spark.memory.storageFraction=0.5 # Storage
```

* Reserved Memory (예약된 메모리) : Spark를 위해 하드코딩된 메모리
* Spark Memory
  * **Execution Memory(Operation)** : Tasks들을 실행하는데 필요한 메모리
  * **Storage Memory(Caching)** : 캐시 데이터, Broadcast 변수등의 메모리
* User Memory : UDF 구조, 스파크 내장 메타 데이터, RDD lineage나 Dependency를 관리할 때 사용하는 메모

### Memory Outside of JVM(Overhead Memory)

* <mark style="color:orange;">**OffHeap Memory**</mark> : **네트워크 버퍼**(셔플링, 외부 저장소에서 파티션을 읽을 때)등에 사용하거나 **Tungsten**(Storage Memory나 Execution Memory에 사용될 떄)에 사용됩니다.
* External process memory : SparkR, PythonR에 관한 외부 메모리

## 메모리 관리

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

그렇다면, Spark에서 Job이 실행되었다면 Execution Memory에 Thread들이 실행될 것입니다. 그러나 thread의 용량이 Execution Memory의 허용치를 넘었면 Storage Memory를 빌려 사용할 수 있습니다. 다만 비었을 가정에 말이죠. 만약 Storage Memory가 어느정도 채워있다면 Disk에 자장하는 방법이 있습니다. 이마저도 방법이 없다면 Out of Memory가 발생하게 됩니다.
