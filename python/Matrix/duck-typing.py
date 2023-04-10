"""
- dict 인스턴스에 들어 있는 내용을 이터레이션할 때 키를 삽입한 순서대로 돌려받는다는 사실에 의존할 수 있다.
- 파이썬은 딕셔너리는 아니지만 딕셔너리와 비슷한 객체를 만들 수 있게 한다. 하지만 키 삽입 순서를 보존할 수 없다.
- 딕셔너리와 비슷한 클래스를 조심스럽게 다루기 위해 
  - 삽입 순서에 의존하지 않고 코드 작성
  - 실행 시점에 명시적으로 딕셔너리 타입 검사
  - 타입 애너테이션과 정적 분석으로 딕셔너리 값 요구
"""

"""
Python 3.5 이전에는 딕셔너리에 대해 이터레이션을 수행하면 삽입 순서와 달리 임의의 순서로 돌려줬었다.
이유는 그당시 딕셔너리 구현이 난수 씨앗값을 사용하는 해시 테이블 알고리즘으로 만들어져서 실행시 마다 난수값과 hash가 어울려져 순서가 일치하지 않았다.
하지만 3.6 부터 개선이 되었다.
"""

votes = {
    'otter' : 1281,
    'bear' : 587,
    'fox' : 863
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True) # ['otter', 'fox', 'bear']
    for i, name in enumerate(names, 1):
        ranks[name] = i
        
def get_winner(ranks):
    return next(iter(ranks))
    
ranks = {}
populate_ranks(votes, ranks)
print(ranks) # {'otter': 1, 'fox': 2, 'bear': 3}
winner = get_winner(ranks)
print(winner) # otter

# 만약에 등수를 보여주는 게 아니라 알파벳 순으로 표시를 해야한다고 하면 어떻게 할까
# collections.abc 모듈을 사용해 알파벳 순서대로 이터레이션 하는 클래스를 정의할 수 있다.

from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
        
    def __getitem__(self, key):
        return self.data[key]
        
    def __setitem__(self, key, value):
        self.data[key] = value
        
    def __delitem__(self, key):
        del self.data[key]
        
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
            
    def __len__(self):
        return len(self.data)
        
sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

# 여기서는 SortedDict를 사용하므로 삽입 순서로 이터레이션하지 않는다.
# 즉, 알파벳 순서 일등인 bear가 반환된다.

# 위 문제를 해결하기 위해 세가지 방법이 있다.
# 1. 삽입 순서에 의존하지 않고 get_winner 코드를 작성하는 것이다. 

def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name
            
winner = get_winner(sorted_ranks)
print(winner)

# 2. 실행 시점에 명시적으로 딕셔너리 타입 검사 (ranks의 타입이 우리가 원하는 타입인지 검사)
def get_winner(ranks):
    if not isinstance(ranks, dict): # 딕셔너리 타입을 흉내냈기 때문에 오류가 발생한다.
        raise TypeError('dict 인스턴스가 필요합니다.')
    return next(iter(ranks))
get_winner(sorted_ranks)


# 3. 타입 애너테이션과 정적 분석으로 딕셔너리 값 요구 (MutableMapping이 아니라 dict 인스턴스가 되도록 강제화)
from typing import Dict, MutableMapping
def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
        
def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))
    
class SortedDict(MutableMapping[str, int]):
    ...
    
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

# 앞의 코드에 타입 애너테이션을 붙이고 mypy도구로 엄격한 모드로 사용한다.
# python3 -m mypy --strict example.py