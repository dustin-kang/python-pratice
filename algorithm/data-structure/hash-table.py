class HashTable:
    def __init__(self):
        # 해시 테이블의 공간 : 100
        self.table_length = 100
        self.hash_table = list([None for i in range(self.table_length)])
        
    def hash_function(self, key):
        # 해시 함수
        ord_sum = 0
        for letter in key:
            ord_sum += ord(letter)
        return ord_sum % self.table_length
        
    def insert(self, key, value):
        # hash_value(=key) , value
        hash_value = self.hash_function(key)
        self.hash_table[hash_value] = value
        
    def read(self, key):
        # key 값을 이용해 값 반환
        hash_value = self.hash_function(key)
        return self.hash_table[hash_value]
        
    def print(self):
        for idx, value in enumerate(self.hash_table):
            if value: # is not None
                print(idx, value)

ex_table = HashTable()
ex_table.insert('Kang', 7459)
ex_table.insert('Kim', 8345)
ex_table.insert('Lee', 7500) # Idi 와 동일한 해시값을 가짐
ex_table.insert('Idi', 4523) # 해결을 위해 넓은 범위의 숫자를 생성할 수 있도록 수정이 필요함.
print(ex_table.read('Kang'))

ex_table.print()