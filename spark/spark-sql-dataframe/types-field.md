# types : Field 생성하기

### StructType

StructType에 포함된 `StructField` 를 반복적으로 적용할 수 있는 기능입니다. **만약 데이터프레임에 헤더가 없는 경우 `Field`를 만들어주는 기능**을 하고 있습니다.

```python
from pyspark.sql import (
    SparkSession,
    functions as f,
    Row,
    types as t
)
```

먼저 `types` 라는 모듈을 불러옵니다.

```python
# types.StructField(name, dataType, nullable=True, metadata=None)
table_schema = t.StructType([
    t.StructField("country", t.StringType(), True),
    t.StructField("temperature", t.FloatType(), True),
    t.StructField("observed_date", t.StringType(), True)])

csv_file_path = "file:///home/jovyan/work/sample/temp_with_date.csv"
df = spark.read.schema(table_schema).csv(csv_file_path)
```

StructType 내에 StructField를 구성하여 Schema를 만들어줍니다. 그런 다음, sparkSession을 통해 Schema와 데이터가 담긴 데이터파일(csv)을 읽어들이면 됩니다.
