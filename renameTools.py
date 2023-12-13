# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
# Author Start
# hint Date: 2023-10-30 12:41:54
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2023-10-30 12:41:55
# hint Description:
# hint FilePath: \PythonSmallTools\renameTools.py
# Author End

import os
import re
import numpy
import datetime
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from ModifiedLogging import modifiledLogging as ML

class tools:
    # RE 用于计算并判断是否包含相似字符串
    def ContainStr(self, source_str: str, target_str: str) -> bool:
        pattern = r'\s+|[_-]'
        list_base = re.split(pattern, source_str.lower())
        list_target = re.split(pattern, target_str.lower())
        score = 0
        for i in list_target:
            if i in list_base:
                score += 1
        if score / len(list_base) > 1/2:
            return True
        else:
            return False

    # DONE 获取文件夹的大小
    def Count_DirSize(self, dir: str, taskID: str, sizeSetting: str = "GB") -> float:
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

    # DONE 获取文件夹下的子文件夹的图片/视频数量
    def Count_Dir_PicAndVedio(self, dir: str) -> tuple[int, int]:
        picCount, videoCount = 0, 0
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.split(".")[-1] in self.picFile:
                    picCount += 1
                elif file.split(".")[-1] in self.vedioFile:
                    videoCount += 1
        return picCount, videoCount

    # DONE 获取文件夹的元信息
    def Get_Dir_MetaInfo(self, path: str, sizeSetting: str = "GB") -> dict:
        subDirMetaInfo = {}
        for dir in os.listdir(path):
            token = os.path.join(path, dir)
            if os.path.isdir(token):
                subdir_count_id = self.progress.add_task(description=dir)
                pics, videos = self.Count_Dir_PicAndVedio(token)
                video_meta = "" if (videos != 0) else f"{videos}V"
                MetaInfo = f"{pics}P" + video_meta
                subDirMetaInfo[dir] = f"{MetaInfo}_{self.Count_DirSize(token, subdir_count_id, sizeSetting):.2f} GB"
        return subDirMetaInfo

# RE 重做重命名工具
class rename_tools:
    def __init__(self, progress: Progress, filePath: str) -> None:
        self.progress = progress
        self.logger = ML(
            r"./RenameLog", f"Renamelog-{datetime.datetime.today().strftime('%Y-%m-%d')}").MakeLogging()
        self.picFile = ["jpg", "png", "jpeg", "bmp", "gif", "webp", "psd", "svg", "tiff",
                        "tif", "raw", "heif", "indd", "jp2", "jxr", "hdp", "wdp", "bpg", "ico", "cur"]
        self.vedioFile = ["mp4", "avi", "mov", "wmv",
                          "flv", "f4v", "f4p", "f4a", "f4b", "rmvb"]
        self.tools = tools()

    # RE 重命名文件夹，增加元信息
    def Add_MetaInfo(self, path: str = None, add_rule: str = "M") -> None:
        if path == None:
            raise Exception("Path is None")
        dirSize = self.tools.Get_Dir_MetaInfo(path)

        for dir in os.walk(path).__next__()[1]:
            # HINT 原文件名
            sub_dir = os.path.join(path, dir)
            # Rename Rules
            if add_rule == "A":
                new_name = f"{dir}-[{dirSize[dir]}]"
            elif add_rule == "M":
                patten_model = r"(@M.*?\[.*?\])"
                modelName = re.findall(patten_model, dir)
                if len(modelName) == 0:
                    self.logger.debug(f"Error Name: {dir}")
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

    # RE 重命名文件工具
    def RT_RenameFiles(self, path: str, inject: str = "", controller: int = 0) -> None:
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
                            self.logger.info(
                                f"Rename: \"{file_path_current}\" -> \"{new_file_path}\"")
                        elif file_path_current == new_file_path:
                            self.logger.debug("New File is the Same Name")
                        else:
                            self.logger.debug("This File Is Exist")
                else:
                    self.logger.debug("Inject is Empty")

    # RE 替换特定图片的名字（对于特定文件簇）
    def RT_RenameSpecificPic(self, model: str) -> None:
        if model == "Alpha" or "alpha" or "A" or "a":
            Key = '@WallPaperAlpha_'
            AddName = f"@WallPaperAlpha_{datetime.datetime.today().strftime('%Y-%m-%d_%H-%H')}_"
            root, dirs, files = os.walk(self.filePath).__next__()
            rsp_task = self.progress.add_task(
                description="RT_RenameSpecificPic", total=len(files))
            for file in files:
                self.progress.advance(rsp_task, advance=1)
                if file.endswith(".png") or file.endswith(".jpg"):
                    if file.startswith(Key) == True:
                        self.logger.debug(
                            f"Find: {os.path.join(root, file)}, Donot Rename")
                    else:
                        file_path_current = os.path.join(root, file)
                        new_file_path = os.path.join(
                            root, f"{AddName}{file:15}")
                        os.rename(file_path_current, new_file_path)
                        self.logger.info(
                            f"Rename: {file_path_current} -> {new_file_path}")
        else:
            raise Exception("Model Name Error")

    # BUG: 缩短文件名
    def RT_Short(self) -> None:
        for root, dirs, files in os.walk(self.filePath):
            current = root.split("\\")[-1]
            for file in files:
                if file.split(".")[-1] == "jpg" or "png":
                    shortSTR = self.RT_SplitSTR(file, current)[-1]
                    new_name = f"{file}-{shortSTR}"
                    os.rename(os.path.join(root, file),
                              os.path.join(root, new_name))
                    self.logger.info(f"Rename: {file} -> {new_name}")

if __name__ == "__main__":

    toggle = True
    base_path = r"D:\.@\@PIC\@T\@M#B#[Serena Wood]-[33.56 GB]@Enrich@Unique #Delete"
    test_path = r"D:\AxMyWorkBench\PythonProject\TestData\DingTest"

    pathList = [
        r"E:\BaiduNetdiskDownload\1210\眼酱大魔王 PS：httpswww.91xiezhen.top"
    ]
    for path in pathList:
        with Progress(TextColumn("[progress.description]{task.description}"),
                      BarColumn(),
                      TimeRemainingColumn(),
                      TimeElapsedColumn()) as progress:
            renameTools = rename_tools(progress)
