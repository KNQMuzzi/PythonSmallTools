# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2023-10-30 12:41:54
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2023-10-30 12:41:55
# hint Description:
# hint FilePath: \PythonSmallTools\renameTools.py
# Author End

import os, re, numpy, datetime
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from ModifiedLogging import modifiledLogging as ML

class RT:
    def __init__(self,
                 progress:Progress,
                 filePath:str,
                 renameRule:str = None,) -> None:
        self.progress = progress
        self.filePath = filePath
        self.renameRule = renameRule
        self.logger = ML(r"./RenameLog", f"Renamelog-{datetime.datetime.today().strftime('%Y-%m-%d')}").MakeLogging()

    # HINT 用于计算并判断是否包含相似字符串
    def RT_ContainStr(self, source_str:str, target_str:str) -> bool:
        pattern = r'\s+|[_-]'
        list_base = re.split(pattern, source_str.lower())
        list_target = re.split(pattern, target_str.lower())
        score = 0
        for i in list_target:
            if i in list_base:
                score += 1
        if score / len(list_base) > 7/9:
            return True
        else:
            return False

    # HINT 获取文件夹的大小
    def RT_GetDirSize(self, dir:str, taskID:str, sizeSetting:str = "GB") -> float:
        size = 0
        for root, dirs, files in os.walk(dir):
            for name in files:
                size += os.path.getsize(os.path.join(root, name))
                self.progress.advance(taskID, advance=1)
        if sizeSetting == "GB" or "gb":
            size = size / 1024 / 1024 / 1024
        elif sizeSetting == "MB" or "mb":
            size = size / 1024 / 1024
        else:
            raise Exception("SizeSetting Error Should Be GB or MB")
        return size

    # HINT 获取文件夹下的子文件夹的大小
    def RT_SubDirSize(self, sizeSetting:str = "GB") -> dict:
        subDirSize = {}
        for dir in os.listdir(self.filePath):
            if os.path.isdir(os.path.join(self.filePath, dir)):
                taskCountSize = self.progress.add_task(description = dir)
                subDirSize[dir] = f"{self.RT_GetDirSize(os.path.join(self.filePath, dir), taskCountSize, sizeSetting):.2f} GB"
        return subDirSize

    # HINT 重命名文件工具
    def RT_RenameFiles(self, path:str, inject:str = "", controller:int = 0) -> None:
        '''
        :description:
        :param path [*]
        :param contorller [int]
            -1: 不重命名文件
            0: 不重命名相似文件
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

                self.RT_RenameFiles(file_path_current, filename, controller)
            else:
                # HINT 判断是否是初始的调用，若运行，此时的inject是本级文件夹名字
                if inject != "":
                    # HINT 新的文件名(基础)
                    new_file_path = os.path.join(path, inject)
                    # HINT 扩展名
                    if os.path.splitext(filename)[1] != "":
                        file_extension = os.path.splitext(filename)[1]
                    else:
                        file_extension = ".png"
                    # HINT 判断是否包含重命名注入的分数阈值
                    if self.RT_ContainStr(filename, inject):
                        if controller == 0:
                            new_file_path = f"{file_path_current}"
                        else:
                            new_file_path = f"{new_file_path}_File_{filenameList.index(filename):04d}{file_extension}"
                    elif self.RT_ContainStr("_cover", filename) == True:
                        new_file_path = f"{new_file_path}_CoverS{file_extension}"
                    # HINT 若文件太几把长，直接重新命名
                    elif len(filename) > 50:
                        new_file_path = f"{new_file_path}_File_{filenameList.index(filename):04d}{file_extension}"
                    else:
                        new_file_path = f"{new_file_path}_{filename}"

                    # HINT 判断新的文件名是否存在，不存在就重命名
                    if controller != -1 and controller != None:
                        if os.path.exists(new_file_path) == False and file_path_current != new_file_path:
                            os.rename(file_path_current, new_file_path)
                            self.logger.info(f"Rename: {file_path_current} -> {new_file_path}")
                        elif file_path_current == new_file_path:
                            self.logger.debug("New File is the Same Name")
                        else:
                            self.logger.debug("This File Is Exist")
                else:
                    self.logger.debug("Inject is Empty")

    # HINT 重命名文件夹，增加大小在文件的末尾
    def RT_AddFileSizeEnd(self, rule = "a") -> None:
        dirSize = self.RT_SubDirSize(self.filePath)
        # HINT 重命名
        for dir_name in os.walk(self.filePath).__next__()[1]:
            # HINT 原文件名
            sourceFileNamePath = os.path.join(self.filePath, dir_name)
            # HINT 修改规则
            if rule == "a":
                new_name = f"{dir_name}-[{dirSize[dir_name]}]"
            if rule == "m" or "M":
                # HINT Find Model Name
                pattenModelNameKeyWord = r"(@M.*?\[.*?\])"
                modelName = re.findall(pattenModelNameKeyWord, dir_name)
                if len(modelName) == 0:
                    self.logger.debug(f"Error Name: {dir_name}")
                    modelName = None
                elif len(modelName) == 1:
                    modelName = modelName[0]
                else:
                    lenList = []
                    [lenList.append(len(i)) for i in modelName]
                    lenList = numpy.array(lenList)
                    modelName = modelName[lenList.argmax()]
                # HINT Find Commit
                pattenCommitKeyWord = r"\](@.*)"
                commit = re.findall(pattenCommitKeyWord, dir_name)
                # HINT 控制重命名的操作
                if modelName != None:
                    new_name = f"{modelName}-[{dirSize[dir_name]}]{commit[0] if len(commit) != 0 else ''}"
                else:
                    new_name = None
            # HINT 控制重命名的操作
            if new_name != None:
                newFileNamePath = os.path.join(self.filePath, new_name)
                os.rename(sourceFileNamePath, newFileNamePath)
            if sourceFileNamePath != newFileNamePath:
                self.logger.info(f"Rename: {dir_name} -> {new_name}")
            else:
                self.logger.debug(f"Same name {dir_name}")

    def RT_RenameSpecificPic(self, model:str) -> None:
        if model == "Alpha" or "alpha" or "A" or "a":
            Key = '@WallPaperAlpha_'
            AddName = f"@WallPaperAlpha_{datetime.datetime.today().strftime('%Y-%m-%d_%H-%H')}_"
            root, dirs, files = os.walk(self.filePath).__next__()
            rsp_task = self.progress.add_task(description = "RT_RenameSpecificPic", total=len(files))
            for file in files:
                self.progress.advance(rsp_task, advance = 1)
                if file.endswith(".png") or file.endswith(".jpg"):
                    if file.startswith(Key) == True:
                        self.logger.debug(f"Find: {os.path.join(root, file)}, Donot Rename")
                    else:
                        file_path_current = os.path.join(root, file)
                        new_file_path = os.path.join(root, f"{AddName}{file:15}")
                        os.rename(file_path_current, new_file_path)
                        self.logger.info(f"Rename: {file_path_current} -> {new_file_path}")
        else:
            raise Exception("Model Name Error")

    def RT_ShortTheFileName():
        pass

if __name__ == "__main__":
    base_path = r"D:\.@\@PIC\@T\@M######[Serena Wood]-[33.56 GB]"
    with Progress(TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeRemainingColumn(),
            TimeElapsedColumn()) as progress:

        RT = RT(progress, base_path)
        RT.RT_RenameFiles(base_path, controller = 0)
        # RT.RT_AddFileSizeEnd(rule = "m")
        # RT.RT_RenameSpecificPic("Alpha")