# -*- coding: utf-8 -*-
# @Time      : 2021/3/24 17:52
# @Author    : JianjinL
# @eMail     : jianjinlv@163.com
# @File      : date_generator
# @Software  : PyCharm
# @Dscription: 


import random

# 年份
year = [str(char) for char in range(1949, 2100)]

# 月份
month_one = [str(char) for char in range(1, 13)]
month_two = ['0' + str(char) for char in range(1, 10)] + [str(char) for char in range(10, 13)]

# 日
day_one = [str(char) for char in range(1, 31)]
day_two = ['0' + str(char) for char in range(1, 10)] + [str(char) for char in range(10, 31)]

# 模式

with open('date.txt', 'w', encoding='utf8') as f:
    for i in range(500000):
        flag = random.randint(1, 106)
        if flag < 30:
            # 不带0
            # 05/30
            text = '{0}/{1}'.format(random.choice(month_one), random.choice(day_one))
            f.writelines(text + '\n')
        elif flag < 60:
            # 带0
            # 05/30
            text = '{0}/{1}'.format(random.choice(month_two), random.choice(day_two))
            f.writelines(text + '\n')
        elif flag < 65:
            # 2013.12-2023.12
            year1 = random.choice(year)
            year2 = str(int(year1) + random.choice([5, 10, 15, 20]))
            month1 = random.choice(month_one)
            if random.randint(1, 10) == 5:
                month2 = random.choice(month_one)
            else:
                month2 = month1
            text = '{0}.{1}-{2}.{3}'.format(year1, month1, year2, month2)
            f.writelines(text + '\n')
        elif flag < 70:
            # 不带0
            # 2013.12-2023.12
            year1 = random.choice(year)
            year2 = str(int(year1) + random.choice([5, 10, 15, 20]))
            month1 = random.choice(month_one)
            if random.randint(1, 10) == 5:
                month2 = random.choice(month_one)
            else:
                month2 = month1
            if random.randint(1, 10) > 4:
                text = '{0}.{1}-{2}.{3}'.format(year1, month1, year2, month2)
            else:
                text = '{0}年{1}月-{2}年{3}月'.format(year1, month1, year2, month2)
            f.writelines(text + '\n')
        elif flag < 75:
            # 带0
            # 2013.12-2023.12
            year1 = random.choice(year)
            year2 = str(int(year1) + random.choice([5, 10, 15, 20]))
            month1 = random.choice(month_two)
            if random.randint(1, 10) == 5:
                month2 = random.choice(month_two)
            else:
                month2 = month1
            if random.randint(1, 10) > 4:
                text = '{0}.{1}-{2}.{3}'.format(year1, month1, year2, month2)
            else:
                text = '{0}年{1}月-{2}年{3}月'.format(year1, month1, year2, month2)
            f.writelines(text + '\n')
        elif flag < 80:
            # 不带0
            # 2009.09.24-2019.09.23
            year1 = random.choice(year)
            year2 = str(int(year1) + random.choice([5, 10, 15, 20]))
            month1 = random.choice(month_one)
            day1 = random.choice(day_one)
            if random.randint(1, 10) == 5:
                month2 = random.choice(month_one)
                day2 = random.choice(day_one)
            else:
                month2 = month1
                day2 = day1
            if random.randint(1, 10) > 4:
                text = '{0}.{1}.{2}-{3}.{4}.{5}'.format(year1, month1, day1, year2, month2, day2)
            else:
                text = '{0}年{1}月{2}日-{3}年{4}月{5}日'.format(year1, month1, day1, year2, month2, day2)
            f.writelines(text + '\n')
        elif flag < 85:
            # 不带0
            # 2009.09.24-2019.09.23
            year1 = random.choice(year)
            year2 = str(int(year1) + random.choice([5, 10, 15, 20]))
            month1 = random.choice(month_two)
            day1 = random.choice(day_two)
            if random.randint(1, 10) == 5:
                month2 = random.choice(month_two)
                day2 = random.choice(day_two)
            else:
                month2 = month1
                day2 = day1
            if random.randint(1, 10) > 4:
                text = '{0}.{1}.{2}-{3}.{4}.{5}'.format(year1, month1, day1, year2, month2, day2)
            else:
                text = '{0}年{1}月{2}日-{3}年{4}月{5}日'.format(year1, month1, day1, year2, month2, day2)
            f.writelines(text + '\n')
        elif flag < 90:
            # 不带0
            # 2009年08月
            year1 = random.choice(year)
            month1 = random.choice(month_one)
            text = '{0}年{1}月'.format(year1, month1)
            f.writelines(text + '\n')
        elif flag < 95:
            # 带0
            # 2009年08月
            year1 = random.choice(year)
            month1 = random.choice(month_two)
            text = '{0}年{1}月'.format(year1, month1)
            f.writelines(text + '\n')
        elif flag < 100:
            # 不带0
            # 2009年08月07日
            year1 = random.choice(year)
            month1 = random.choice(month_one)
            day1 = random.choice(day_one)
            text = '{0}年{1}月{2}日'.format(year1, month1, day1)
            f.writelines(text + '\n')
        elif flag < 105:
            # 带0
            # 2009年08月07日
            year1 = random.choice(year)
            month1 = random.choice(month_two)
            day1 = random.choice(day_two)
            text = '{0}年{1}月{2}日'.format(year1, month1, day1)
            f.writelines(text + '\n')
