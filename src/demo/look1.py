"""
    author: Shawn
    time  : 7/21/18 5:25 PM
    desc  :
    update: Shawn 7/21/18 5:25 PM
"""

from pyecharts import Style
from pyecharts import Geo

# 读取城市数据
city = []

with open('assert/data/sample.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n', ''))


def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)

    return result


# print(all_list(city))

data = []
style = None
for item in all_list(city):
    # print(item)
    if item != '' and item != '铜梁' and item != '海安' and item != '威宁' and item != '西平' and item != '万宁' \
            and item != '薛城' and item != '薛城' and item != '中牟' and item != '博兴' and item != '东方' and item != '大足区' \
            and item != '蒲城' and item != '昌乐' and item != '海盐' and item != '赣榆' and item != '如东' and item != '宁国' \
            and item != '黔西南' and item != '蒙自市' and item != '宜都' and item != '齐河':
        data.append((item, all_list(city)[item]))
        style = Style(
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59"
        )

geo = Geo("《邪不压正》粉丝人群地理位置", "数据来源： Python", **style.init_style)
attr, value = geo.cast(data)
print(attr)
print('----' * 20)
print(value)
geo.add("", attr, value, visual_range=[0, 20],
        visual_text_color="#fff", symbol_size=20,
        is_visualmap=True, is_piecewise=True,
        visual_split_number=4)

geo.render('look1.html')
