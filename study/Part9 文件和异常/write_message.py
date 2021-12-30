filename = 'programming.txt'
# open(filename, 'w') 其中filename为要打开文件的名称，w为我要以写入模式打开（'r'读取模式，'a'附加模式，'r+'可读取也可写入 , 为空则默认为只读模式)
# 注意若写入的文件不存在，则open()将自动创建，若文件已存在，python将在返回文件对象前清空该文件
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love Python.\n")

with open(filename, 'a') as file_object:
    file_object.write("I love creating apps that can run in a browser.\n")
