# 记录生肖，根据用户输入的年份判断生肖。假设1月-12月份一个生肖
# 序列，通过下标和偏移量访问，

chinese_zodiac = '猴鸡狗猪鼠牛虎兔蛇马羊'


# print (chinese_zodiac[0:4])
# print (chinese_zodiac[-1])

year = 2023

print(year % 12)

print (chinese_zodiac[year % 12])





