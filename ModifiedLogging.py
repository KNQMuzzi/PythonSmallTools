###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2023-06-01 20:36:44
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2023-06-08 21:16:49
# hint Description:
    # tdd 自定义的日志生成该文件
# hint FilePath: \RotatE-SimTWD-Re-Rank\RSTWDReRank\codes\Jupiter\ModifiedLogging.py
# Author End

import logging, os

class modifiledLogging:
    '''
    :description:自定义日志文件存储
    :param self [*]
    :param logpath [日志存放路径]
    :param logname [日志名]
    '''
    def __init__(self, logpath:str, logname:str):
        self.logpath = logpath
        self.logname = logname

    # Hint Log Setting
    #TDD: 1. 日志文档需要加入更多的选项集描述 Debug,Info,Warning,Error,Critical
    def MakeLogging(self) -> logging.Logger:
        logger = logging.getLogger(self.logname)
        # 创建一个handler，用于写入日志文件
        filename = os.path.join(self.logpath, self.logname + '.log')
        fh = logging.FileHandler(filename, mode='w+', encoding='utf-8')
        ch = logging.StreamHandler()
        # 定义输出格式(可以定义多个输出格式例formatter1，formatter2)
        formatter = logging.Formatter('%(asctime)s %(message)s')
        # 定义日志输出层级
        logger.setLevel(logging.DEBUG)
        fh.setLevel(logging.DEBUG)
        ch.setLevel(logging.INFO)
        # 为文件操作符绑定格式（可以绑定多种格式例fh.setFormatter(formatter2)）
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

if __name__ == "__main__":

    modifiledLogging = modifiledLogging(r'C:\Users\knqmu\Desktop','test')
    logger = modifiledLogging.MakeLogging()
    logger.info('test')

