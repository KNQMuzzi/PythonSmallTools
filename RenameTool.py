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
import PIL.Image as Image
import time,datetime

# HINT 组件部分
# 获取路径下的全部文件夹名称
def get_all_dir(path:str) -> list:
    dirs = os.listdir(path)
    return [dir for dir in dirs if os.path.isdir(os.path.join(path, dir))]
# 获取路径下的全部文件名称
def get_all_file(path:str) -> list:
    files = os.listdir(path)
    return [file for file in files if os.path.isfile(os.path.join(path, file))]
# 正则匹配
def renamer(string:str, patten:str, template:str) -> str:
    match = re.match(patten, string)
    new_string = re.sub(patten, template, string)
    return new_string
# 获取图片的mate信息
def get_mateinfo(pic_path:str) -> list:
    img = Image.open(pic_path)
    return img._getexif()
# 获取图片的创建、修改时间
def get_picTime(pic_path:str) -> str:
    modTime = os.path.getmtime(pic_path)
    createTime = os.path.getctime(pic_path)
    return datetime.datetime.fromtimestamp(modTime).strftime('%Y-%m-%d_%H-%M'), datetime.datetime.fromtimestamp(createTime).strftime('%Y-%m-%d_%H-%M')

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
# 重命名wallhaven壁纸图片
def rename_wallhaven(path):
    with Progress(TextColumn("[progress.description]{task.description}"),
                 BarColumn(),
                 TextColumn("[progress.percentage]{task.percentage:>3.0f}%")) as progress:
        files = os.listdir(path)
        batch = progress.add_task(description = "改名进度", total = len(files))

        pass
        for file in files:
            if 'wallhaven' in file:
                new_name = file.replace('wallhaven-', '')
                os.rename(os.path.join(path, file), os.path.join(path, new_name))
            progress.advance(batch, advance=1)
        print(f'{len(files)} 改名完成！')



if __name__ == '__main__':
    # 参数设置
    path = 'E:\@Pic\α'
    patten = r'(NO\.\d{3})(.*)'
    repl = r'\1_\2'
    # 函数设置
    # rename_dir_typeA(path, patten, repl)
    # print(get_picTime('E:\@Pic\α\wallhaven-1pevqg.jpg'))

    print(get_all_dir(path))