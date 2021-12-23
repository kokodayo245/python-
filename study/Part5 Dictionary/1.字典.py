# 字典是一系列键——值对。每个键都与一个值相关联
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 添加 新的键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改键值对
alien_0['color'] = 'yellow'
print(alien_0)

alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 根据外星人当前位置速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置 = 老位置 + 增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除 键值对
del alien_0['points']
print(alien_0)
