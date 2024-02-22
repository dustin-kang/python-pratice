"""
SHA-256
해시 구현 문제
https://www.acmicpc.net/problem/10930

파이썬의 해시라이브러리(hashlib)을 이용하면 SHA 256 해시를 구할 수 있다.

"""

import hashlib

input_data = "Baekjoon" # 예시 Baekjoon
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest() # 해시 결과를 문자열 나타내자. (hexdigest)

assert result == "9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857"