# 处理成群的外星人
aliens = []

# 创建30个绿色外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 将前3个外星人颜色设为黄色 速度为10
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)
print("....")
