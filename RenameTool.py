# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2024-06-04 17:09:39
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2024-06-04 17:09:39
# hint Description:
# hint FilePath: \PythonSmallTools\RenameTool.py
# Author End

import re, os, random
from rich.progress import Progress, TextColumn, BarColumn

# HINT 组件部分
# 获取路径下的全部文件夹名称
def get_all_dir(path:str) -> list:
    import os
    dirs = os.listdir(path)
    return [dir for dir in dirs if os.path.isdir(os.path.join(path, dir))]

# 正则匹配
def renamer(string:str, patten:str, template:str) -> str:
    match = re.match(patten, string)
    new_string = re.sub(patten, template, string)
    return new_string

# HINT 主函数部分
# 根据文件夹名称，进行匹配并重命名
def rename_dir_typeA(path, pattern, repl):
    with Progress(TextColumn("[progress.description]{task.description}"),
                 BarColumn(),
                 TextColumn("[progress.percentage]{task.percentage:>3.0f}%")) as progress:

        dirs = get_all_dir(path)
        batch = progress.add_task(description = "改名进度", total = len(dirs))
        for dir in dirs:
            new_dir = renamer(dir, pattern, repl)
            os.rename(os.path.join(path, dir), os.path.join(path, new_dir))
            progress.advance(batch, advance=1)
        print(f'{len(dirs)} 改名完成！')


path = 'E:\BaiduNetdiskDownload\暴击少女喵小吉 PS：www.kkaiq.com'
patten = r'(NO\.\d{3})(.*)'
repl = r'\1_\2'

rename_dir_typeA(path, patten, repl)