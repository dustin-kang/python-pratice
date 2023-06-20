# Speculative Execution

Stage에서 하나의 Task가 다른 Task보다 느린 이유가 Worker Node의 문제일 때 사용하는 방법입니다.

<figure><img src="../../.gitbook/assets/image (12).png" alt="" width="375"><figcaption></figcaption></figure>

* 하드웨어의 문제를 해결합니다.
* 여분의 리소스를 더 사용하기 때문에 메모리 사용이 증가합니다.

```python
# 나머지 Task보다 1.5배 늦게 끝냈을 경 Specular execution을 사용합니다.
spark.speculation.multiplier = 1.5 

# 나머지 Task가 75% 끝났으나 아직 완료하지 못했을 때 Specular execution을 사용합니다.
spark.speculation.quantile = 0.75

```

