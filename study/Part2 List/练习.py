# 3-4
namelist = ['张三', '李四',  '狗蛋']
print(namelist)
# 3-5
print("狗蛋无法赴约")
namelist[2] = '狗剩'
print(namelist)
# 3-6
print("找到一个更大的餐桌，可多邀请3个人了")
namelist.insert(0, '大白')
namelist.insert(2, '大黑')
namelist.append('王五')
print(namelist)
# 3-7
print("情况有变，现在只能邀请2个人")
name = namelist.pop()
print("抱歉！" + name)
name = namelist.pop()
print("抱歉！" + name)
name = namelist.pop()
print("抱歉！" + name)
name = namelist.pop()
print("抱歉！" + name)
print("欢迎你！" + namelist[0])
print("欢迎你！" + namelist[1])
del namelist[0]
del namelist[0]
print(namelist)
