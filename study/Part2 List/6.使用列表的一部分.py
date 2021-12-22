# 切片 索引[0:3] 实际上类似于[0:3) 左闭右开区间
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[:4])
print(players[1:])

# 负数索引返回离列表末尾相应距离的元素 例如：players[-3:] 输出名单上最后3名队员
print(players[-3:])

# 遍历前3名队员
for player in players[:3]:
    print(player.title())
# 复制列表
lol_players = players[:]
lol_players.append('1')
players.append('2')
print(lol_players)
print(players)

# 若直接lol_players = players 则会发现，lol_players和players都添加了3，4
lol_players = players
lol_players.append('3')
players.append('4')
print(lol_players)
print(players)