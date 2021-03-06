# -*- coding: utf-8 -*-
import os
import time
import logging
import inspect
from pathlib import Path
from logging.handlers import RotatingFileHandler


dir = os.path.dirname(__file__)
dir_parent = "logs"
dir_time = time.strftime('%Y-%m-%d', time.localtime())

handlers = {
    logging.NOTSET: os.path.join(dir, dir_parent, dir_time, 'notset.log'),
    logging.DEBUG: os.path.join(dir, dir_parent, dir_time, 'debug.log'),
    logging.INFO: os.path.join(dir, dir_parent, dir_time, 'info.log'),
    logging.WARNING: os.path.join(dir, dir_parent, dir_time, 'warning.log'),
    logging.ERROR: os.path.join(dir, dir_parent, dir_time, 'error.log'),
    logging.CRITICAL: os.path.join(dir, dir_parent, dir_time, 'critical.log'),
}


def createHandlers():
    logLevels = handlers.keys()

    for level in logLevels:
        path = os.path.abspath(handlers[level])
        path = Path(path)
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        # 单文件最大10M
        handlers[level] = RotatingFileHandler(
            path, maxBytes=10485760, backupCount=2, encoding='utf-8')


# 加载模块时创建全局变量
createHandlers()


class TNLog(object):

    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}
        logLevels = handlers.keys()

        for level in logLevels:
            logger = logging.getLogger(str(level))

            logger.addHandler(handlers[level])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[
            2]

        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s] [%s] [%s - %s - %s]\n %s" % (self.printfNow(), level, filename, lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__loggers[logging.CRITICAL].critical(message)


if __name__ == "__main__":
    logger = TNLog()

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
