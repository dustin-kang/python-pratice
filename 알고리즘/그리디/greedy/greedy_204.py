"""
배낭 문제

- 가장 최대 가치를 갖도록 배낭에 물건 넣기
- 물건 = (무게(w), 가치(v))

"""
data_list = [(10, 10), (15, 10), (20, 8), (25, 12), (30, 10)]

def bag(data_list, capacity):
    # 가치 / 무게로 나눠 Sort
    data_list = sorted(data_list, key=lambda x : x[1] / x[0], reverse=True)
    total_value = 0
    details = list()
    
    for data in data_list:
        # 채울 공간이 있는 경우
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        
        # 채울 공간이 없는 경우
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    
    print(details, total_value)

bag(data_list, 30)