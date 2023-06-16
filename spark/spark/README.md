# Spark 아키텍처 이해하기

## Cluster

앞서, [PySpark Runtime 아키텍처](pyspark-architecture.md#pyspark-1)를 이해하는데 어려움을 느낀 분이 있을 것입니다.

내용 중 클러스터라는 개념이 등장하는데, 여기서 클러스터는 <mark style="color:green;">**여러 대의 컴퓨터들을 마치 하나의 컴퓨터로 움직이는 것처럼**</mark> 만드는 것을 말합니다. 클러스터의 특징으로는 아래와 같습니다.

* High Availablity
* Load Balancing
* Parallel Processing

예를 들면, 10개의 Worker들을 하나의 Cluster 처럼 하나의 서버처럼 생각하시면 쉽습니다.

## YARN 아키텍처 이해하기

<figure><img src="../../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption><p>YARN Architecture</p></figcaption></figure>

Hadoop의 YARN 아키텍처를 이해하는데 조금 어려울 수 있습니다.

먼저, Spark Submit이 JobSubmission을 Application Manager에게 제출합니다. 이에 A.Managers는 제출을 수락하고 Application master를 실행하기 위해 Node Manager에게 컨테이너를 설정하라고 합니다.&#x20;

이에 Node Managerrk Container에서 Application Master를 생성하고 이를 실행하기 위해 Resource Manager에게 협상을 통해 리소스를 받아오고 구동이 불가능하면  다른 Slave Node의 Manager에게 Container 실행 명령을 전달합니다.



