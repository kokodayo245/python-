# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 用as给函数指定别名，也可给模块指定别名 例如：import pizza as p
from pizza import make_pizza as a
# make_pizza(15, 'pepperoni')
a(12, 'mushrooms')

# '*'可让python导入模块中所有的函数 例如：from pizza import *
