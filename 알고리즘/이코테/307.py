"""
구현 - 럭키 스트레이트
123402 -> LUCKY
7755 -> READY
"""

value = list(map(int, input()))

length = len(value) // 2

if sum(value[:length]) == sum(value[length:]):
    print("LUCKY")
else:
    print("READY")