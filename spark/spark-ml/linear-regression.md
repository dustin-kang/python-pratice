# Linear Regression

## 데이터 불러오기

Spark ML 라이브러리를 사용하기 위해 데이터는 **Feature** 와 **Label**로 이루어진 데이터여야 한다고 했습니다. `libsvm` 을 사용하는 입력 포맷들은 바로 사용할 수 있으니 `spark.read.format("libsvm").load(path)` 로 데이터를 불러올 수 있지만 일반적인 `csv` 와 같은 데이터들은 <mark style="color:orange;">**VectorAssembler**</mark> 작업이 필요합니다.

### Vector Assembler

Spark ML에서는 Label과 Feature 컬럼 밖에 사용하지 않으므로 **여러 개의 Colums 들을 하나의 Vector로 변경**하는 작업이 필요합니다. [Docs](https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.ml.feature.VectorAssembler.html)

```python
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

asbel = VectorAssembler(
        inputCols=['컬럼이름', '컬럼이름'],
        outputCols='벡터화_컬럼_이름')
        
tr_data = asbel.transform(df)
tr_data.printSchema() # 데이터 자료형은 Vector 입니다.
# feature_vectors: vector (nullable = true) 

data = tr_data.select('label', 'feature_vectors')       
```

### 훈련/테스트 데이터 쪼개기

훈련 데이터(Train Set)과 테스트 데이터(Test Set)를 쪼개봅시다. [Docs](https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.DataFrame.randomSplit.html?highlight=randomsplit#pyspark.sql.DataFrame.randomSplit)

```python
train, test = data.randomSplit([0.7, 0.3])

train.describe().show()
test.describe().show()
```

여기서 데이터 세트를 가르는 규칙이 존재합니다.&#x20;

* 훈련 데이터 세트는 테스트 데이터 세트보다 많아야 합니다.
* 두 세트 간의 종복 데이터는 최대한 없어야 합니다.
* 두 세트의 타킷 클래스 비율이 균등하게 있어야 합니다.

## 모델 학습 및 추론

본격적으로 쪼개진 데이터에 학습을 진행합니다.

머신러닝 모델에서는 다양한 종류가 존재합니다.

* Regression(회귀) : 연속적인 값의 라벨을 예측하는 모델을 말합니다. e.g. 몸무게
* Classifier(분류) : 불 연속적인값의 라벨을 예측하는 모델을 말합니다. e.g. 암 유무
* Clustering(군집화) : 어떠한 정보없이 특정 패턴이나 규칙을 기준으로 예측하는 모델을 말합니다. 비지도 학습에 속합니다.

```python
from pyspark.ml.regression import LinearRegression

lr = LinearRegression(
    featuresCol='features', # 속성
    labelCol='label', # 레이블
    predictionCol='prediction', # 예측 컬럼
    maxIter=10, # 반복수 <- 하이퍼 파라미터
    regParam=0.3, # 파라미터 <- 하이퍼 파라미터
    elasticNetParam=0.8 # <- 하이퍼 파라미터
)

lr_model = lr.fit(training) # 학습
test_result = lr_model.evaluate(test) # 추
```

```python
test_result.residuals.show()
```

`residuals` 을 통해 실제값과 예측값의 차이를 확인합니다.&#x20;

## 모델 평가

머신러닝 알고리즘에는 분류 모델이나 회귀모델이나 다양한 평가지표(Metrics)들이 존재합니다.

* [Regression 평가지표](https://github.com/dongwoodev/dataStudy/blob/main/ML/lesson/011\_Regression\_%ED%8F%89%EA%B0%80%EC%A7%80%ED%91%9C.md)
* [Classifier 평가지표](https://github.com/dongwoodev/dataStudy/blob/main/ML/lesson/014\_Classifier\_%ED%8F%89%EA%B0%80%EC%A7%80%ED%91%9C.md)

```python
print(test_output.rootMeanSquaredError)
print(test_output.r2)
data.describe().show()
```

```python
predictions = lr_model.transform(test)
predictions.show()
```

실제로 Test데이터 예측된 결과를 반영합니다.

