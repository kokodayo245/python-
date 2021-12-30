# 读取文件
# open()打开文件,并返回一个表示文件的对象
# with表示不再需要访问文件后将其关闭
with open('pi_digits.txt') as file_object:
    # read()读取文件
    contents = file_object.read()
    print(contents)
# 请注意，反斜杠有两个，因为每个反斜杠需要由另一个反斜杠字符来转义
with open('D:\\python code\\study\\code.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件的内容
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
