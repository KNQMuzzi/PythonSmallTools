# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2023-10-15 23:29:49
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2023-10-15 23:29:49
# hint Description:
# hint FilePath: \RotatE-SimTWD-Re-Rankd:\AxMyWorkBench\PythonProject\SmallTools\Steam_Validator.py
# Author End=
import re, json, os, datetime

baseSTR = r"""
1.YMFCM9711.5DNKBH821.5K6X9K8
2.VKQ8YN712.PY93PM522.TYFH3Y2
3.6B2QG6813.B45NFQ823.4Y97HJ6
4.YY7TDX214.DMCM3C724.QCMR6V5
5.MXJPV7215.28R9DP625.K8K9KM5
6.DXJG6X616.N5MCBP726.N5B8KJ5
7.4DFQ4B717.M4KX26827.9P5MBQ4
8.TGWKJ8318.MRHWK7828.WTTFBX7
9.X46J3C719.9JYD2F729.9JDP2W2
10.QX4XJQ220.BYR23T830.6N5X446
"""

def getSteamValidatorID(baseSTR):
    code_dict = {}
    pattern = re.compile(r'(\d*?)\.(.{7})')
    for line in baseSTR.split('\n'):
        if line:
            match = pattern.findall(line)
            for item in match:
                if len(item[0]) == 1:
                    key = '0' + item[0]
                    code_dict[key] = item[1]
                else:
                    code_dict[item[0]] = item[1]
    code_dict = dict(sorted(code_dict.items(), key = lambda x: int(x[0])))
    return code_dict

if __name__ == '__main__':
    # str_input = input('请输入Steam验证器ID：')
    dict = getSteamValidatorID(baseSTR)
    json_name = "SteamValidatorID_" + datetime.datetime.now().strftime("%Y-%m-%d") + "_.json"
    with open(os.path.join("D:\AxMyWorkBench\PythonProject\SmallTools\SteamValidatorID", json_name), "w") as f:
        json.dump(dict, f, indent=4)
    print(f"Steam验证器ID已保存至{json_name}")
