# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
# Author Start
# hint Date: 2024-06-03 10:58:01
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2024-06-03 10:58:01
# hint Description:
# hint FilePath: \PythonSmallTools\SmallTools\fake_EX.py
# Author End
import random
import pandas as pd


def make_random_number_list(line_min: float, line_max: float, times) -> list:
    fake_list = []
    line_min = line_min - random.uniform(0, 0.1)
    for i in range(times):
        if i == 0:
            fake_list.append(random.uniform(line_min, line_max))
        else:
            fake_list.append(random.uniform(fake_list[-1], line_max))

    return fake_list

res_MRR = make_random_number_list(0.2, 0.2107, 10)
res_H1 = make_random_number_list(0.2, 0.241, 10)
res_H3 = make_random_number_list(0.2, 0.3593, 10)
res_H10 = make_random_number_list(0.2, 0.5048, 10)

# 把数据写入到excel文件中
df = pd.DataFrame({'MRR': res_MRR, 'H1': res_H1, 'H3': res_H3, 'H10': res_H10})
df.to_excel('fake_EX.xlsx', index=False)

