from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time, os, re
from tqdm import tqdm

def factorial(n, bar:tqdm):
    bar.update(1)
    time.sleep(0.01)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1, bar)

def factorialNew(n, progress:Progress, taskID):
    progress.advance(taskID, advance=1)
    time.sleep(0.01)
    if n == 1:
        return 1
    else:
        factorialNew(n-1, taskID)
class RT:
    def RT_GetDirSize(self, progress:Progress, dir:str, sizeSetting:str = "GB") -> float:
        size = 0
        taskName = dir.split("\\")[-1]
        taskCountSize = progress.add_task(description = taskName)
        for root, dirs, files in os.walk(dir):
            for name in files:
                size += os.path.getsize(os.path.join(root, name))
                progress.advance(taskCountSize, advance=1)
        if sizeSetting == "GB" or "gb":
            size = size / 1024 / 1024 / 1024
        elif sizeSetting == "MB" or "mb":
            size = size / 1024 / 1024
        else:
            raise Exception("SizeSetting Error Should Be GB or MB")
        return size

    def RT_SubDirSize(self, progress:Progress, path:str, sizeSetting:str = "GB") -> dict:
        subDirSize = {}
        for dir in os.listdir(path):
            if os.path.isdir(os.path.join(path, dir)):
                subDirSize[dir] = self.RT_GetDirSize(progress, os.path.join(path, dir), sizeSetting)
        return subDirSize

with Progress(TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            TimeElapsedColumn()) as progress:

#     factorialNew(100, batch_tqdm)

    rt = RT()
    path = r"E:\@S\@M"
    dict = rt.RT_SubDirSize(progress, path)
    print(dict)