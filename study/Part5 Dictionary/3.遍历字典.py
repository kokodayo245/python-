user_0 = {
    'username': 'Dijkstra',
    'first': 'enrico',
    'last': 'fermi',
    }
# 声明key和value两个变量
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'a': 'python',
    'b': 'c',
    'c': 'java',
    'd': 'python'
    }
# 方法key()提取字典中的键，并赋值给name
for name in favorite_languages.keys():
    print(name.title())
# 注意key()实际上返回的是一个列表
print(favorite_languages.keys())

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())

# 使用集合(set，类似于列表，但每个元素都必须是独一无二)来剔除重复项
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
