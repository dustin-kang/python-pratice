# PySpark Architecture

## &#x20;Pyspark 사용해보기

Juypter Notebook을 열게되면 Python 코드를 작성할 수 있는 문서를 만들 수 있습니다.

#### SparkContext

```python
import pyspark

sc = pyspark.SparkContext('local[*]')
```

파이썬 라이브러리로 `pyspark`를 불러옵니다.&#x20;

Pyspark 라이브러리에서 **`SparkContext`**라는 클래스를 사용할 수 있습니다. &#x20;



### pySpark 아키텍처 이해하기

SparkContext라는 클래스가 물리적으로 생성되는 과정을 알 필요 있습니다.&#x20;

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt="" width="563"><figcaption><p>Pyspark Dataflow</p></figcaption></figure>

<mark style="color:green;">**우선, Spark는 JVM 위에서 동작합니다.**</mark> Python Driver가 직접적으로 Spark Core에 접근할 방법은 없죠. 그렇기 때문에 Python Driver는 JVM을 통해서 Spark Core에 접근이 가능합니다.

그렇다면 위 PySpark가 실행되는 프로세스를 봅시다.

Python에서 PySpark를 실행하려면 Python이 Java의 Spark를 실행하기 위해 Py4j라는 프로그램이 필요로 합니다. Py4j를 통해 JVM을 실행시킬 수 있습니다. JVM을 통해 Spark Context를 생성할 수 있습니다. 그리고 Spark Context는 Worker로 PySpark를 구동시킬 수 있는 것입니다.&#x20;

**그렇다면 Cluster에 왜 Python Worker가 존재할까요?**

만약 우리가 Python Library가 필요로 할때, Spark Worker만으로는 Pandas나 Numpy와 같은 Python Library를 실행시킬 수 없습니다. 파이썬 라이브러리를 실행시키 위해 Python Worker가 필요한 것입니다. 그리고 이 Worker에게는 파이썬 Library가 반드시 설치되있어야 합니다.

###



## 참고

* [https://surgach.tistory.com/105](https://surgach.tistory.com/105)
