# Spark on Cloud

## AWS Elastic MapReduce(EMR) 클러스터를 만들어 스파크 사용하기

#### 1. 먼저 AWS Console 내 EC2-Key Pairs(키 페어)로 들어갑니다.

여기서 저희는 키 페어를 생성해낼 것입니다. Cluster 안으로 들어가려면 키가 필요하기 때문이죠. Private Key는 따로 갖고 서버에서는 Public Key를 가지게 됩니다. 여기서 두 키를 통해 서버를 들어갈 수 있게 됩니다.

<figure><img src="../.gitbook/assets/Screenshot 2023-06-23 at 18.19.02.png" alt="" width="375"><figcaption></figcaption></figure>

다운받은 `privateky.pem` 파일을 빈 디렉토리에 넣어줍니다. 그리고 키의 권한을 파일 소유자 권한만 읽기 전용으로 변경합니다.&#x20;

#### 2. EMR에서 Cluster를 생성합니다.

![](<../.gitbook/assets/Screenshot 2023-06-23 at 18.30.56.png>)

* EMR Release : AWS에서 만든 EMR 릴리즈 스택입니다.
* 프라이머리 : Master Node
* 코어 : 디스크 공간을 사용할 수 있습니다.
* 테스크 : 디스크 공간을 사용할 수 없습니다.&#x20;
* EBS\_root\_Volume : 인스턴스 마다 얼마나 디스크 공간을 지정할 건지 지정합니다.
* Cluter Termination : 언제 Termination을 할것인지

