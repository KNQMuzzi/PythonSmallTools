# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2023-10-30 12:41:54
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2023-10-30 12:41:55
# hint Description:
# hint FilePath: \PythonSmallTools\renameTools.py
# Author End

import os, re

def RT_ContainStr(str, target_str):
    pattern = r'\s+|[_-]'
    list_base = re.split(pattern, str.lower())
    list_target = re.split(pattern, target_str.lower())
    score = 0
    for i in list_target:
        if i in list_base:
            score += 1
    if score / len(list_base) > 7/9:
        return True
    else:
        return False


def RT_SourceDirName(path, rename_inject = "", controller = 0):
    '''
    :description:
    :param path [*]
    :param rename_inject [*]
    :param contorller [int]
        0. 不重命名相似文件
        1: 重命名相似文件
    :return [*]
    '''
    # HINT 读取文件夹下的文件名列表
    filenameList = os.listdir(path)
    for filename in filenameList:
        # HINT 拼接文件路径，是当前的文件名
        file_path_current = os.path.join(path, filename)
        # HINT 判断是否是文件夹
        if os.path.isdir(file_path_current):
            # HINT 如果是文件夹，递归调用，将文件夹的名字作为参数传入
            RT_SourceDirName(file_path_current, filename, controller)
        else:
            # HINT 判断是否是初始的调用，若运行，此时的inject是本级文件夹名字
            if rename_inject != "":
                # HINT 新的文件名(基础)
                new_file_path = os.path.join(path, rename_inject)
                # HINT 扩展名
                if os.path.splitext(filename)[1] != "":
                    file_extension = os.path.splitext(filename)[1]
                else:
                    file_extension = ".png"
                # HINT 判断是否包含重命名注入的分数阈值
                if RT_ContainStr(filename, rename_inject):
                    if controller == 0:
                        new_file_path = f"{file_path_current}"
                    else:
                        new_file_path = f"{new_file_path}_File_{filenameList.index(filename):04d}{file_extension}"
                elif RT_ContainStr("_cover", filename) == True:
                    new_file_path = f"{new_file_path}_CoverS{file_extension}"
                # HINT 若文件太几把长，直接重新命名
                elif len(filename) > 80:
                    new_file_path = f"{new_file_path}_File_{filenameList.index(filename):04d}{file_extension}"
                else:
                    new_file_path = f"{new_file_path}_{filename}"

                # HINT 判断新的文件名是否存在，不存在就重命名
                if os.path.exists(new_file_path) == False and file_path_current != new_file_path:
                    os.rename(file_path_current, new_file_path)
                    print(f"Rename: {file_path_current} -> {new_file_path}")
                elif file_path_current == new_file_path:
                    print("New File is the Same Name")
                else:
                    print("This File Is Exist")
            else:
                print("Rename_Inject OR Filename_Contain_Rename_Inject")

if __name__ == "__main__":
    base_path = r"E:\@S\@A\@M#C#[Sirena Milano]-[4.26 GB]R"
    RT_SourceDirName(base_path)
