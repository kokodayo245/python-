fruits = ['葡萄', '西瓜', '香蕉']
print(fruits)

# 列表 ，类似于c中的数组，从0开始
print(fruits[0] + fruits[1])

# 方法 append()可将元素添加到列表末尾
fruits.append('苹果')
print(fruits)

# 方法 insert()可在列表任何位置插入元素
fruits.insert(2, '山竹')
print(fruits)

# del 可删除元素
del fruits[4]
# 删除'苹果'
print(fruits)

# 方法 pop() 默认删除列表末尾元素
popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits)
# pop()也可删除指定位置的元素
fruits.pop(0)
print(fruits)
# 当你要从列表中删除一个元素时，可用 del 也可用 pop(), 如果你在删除元素后还要继续使用那个被删除的元素的话，就使用pop(),否则用 del

# 若你不知道要删除元素的位置，可使用remove(),来根据值来删除
fruits.remove('西瓜')
print(fruits)
