# 方法 sort() 可对列表元素按字母顺序进行排序，但它是不可逆，是永久的
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
# 也可逆序排序
cars.sort(reverse=True)
print(cars)

# 函数 sorted()可对列表进行临时排序，不影响原列表的顺序
print(sorted(cars))
print(cars)

# 方法 reverse() 可反转排序顺序，注意是 反转，不是逆序！ 同样是永久改变列表顺序，但若想回到原始顺序只需再调用一次reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# 函数 len()可确定列表长度
length = len(cars)
print(length)