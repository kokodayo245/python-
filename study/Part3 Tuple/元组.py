# 元组：不可变的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值，即重新定义整个元组

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)