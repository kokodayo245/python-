import json
numbers = [2, 3, 4, 5, 6, 7]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    #  json.dump(numbers, f_obj)存储数据 ， numbers为要存储的数据，f_obj为存储数据的文件对象
    json.dump(numbers, f_obj)

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
