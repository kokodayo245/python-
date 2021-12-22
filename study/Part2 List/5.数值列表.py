# 函数 range(1, 5) 生成1~4
for value in range(1, 5):
    print(value)

# 函数list()将range()的结果转化为列表
numbers = list(range(1, 5))
print(numbers)
# range() 还可以指定步长，打印1~10的偶数
even_numbers = list(range(2, 11, 2))
print(even_numbers)

digits = [1, 2, 3, 4, 5, 6]
print(max(digits))
print(min(digits))
print(sum(digits))


