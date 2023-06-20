# Spark ML

## MLlib

Spark의 **머신러닝을 만들기위한 툴**로 아래와 같은 도구들을 제공합니다.

```python
py.spark.ml 
# DataFrame Based
```

* **ML Algorithms** : classification, regression, clustering collaborative filtering
* **Featurization** : feature extraction(특징 추출), transformation (변환) dimensionality reduction(차원 감소), selection (차원 선택)
* **Pipelines** : constructing, evaluating, tuning ML pipeline
* **Persistence** : ML 모델이나 파이프라인을 저장
* **Utilities** : 선형 대수, 분석, 데이터 핸들링 등

#### 장점

사용하기 쉽고 방대하게 사용할 수 있습니다.

#### 단점

<mark style="color:orange;">**데이터 포맷이 정해져있습니다.**</mark> 예를 들어서, Supervised Learning의 경우 **Features와 Labels**, Unsupervised Learning의 경우 **Features**만 담겨있는 데이터여야 합니다.

* Features(특성) : 입력 변수를 의미합니다. &#x20;
* Label(라벨) : 예측 변수를 의미합니다. 특성들을 통해 라벨을 예측한다고 볼 수 있습니다.

{% embed url="https://spark.apache.org/docs/latest/ml-guide.html" %}
