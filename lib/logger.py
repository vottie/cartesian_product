# coding:utf-8

from logging import getLogger, FileHandler, Formatter, DEBUG

class Logger(object):
    filename = 'debug.log'
    level = DEBUG
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(self, name, **kwargs):

        if 'filename' in kwargs:
            self.fmt = kwawgs['fmt']

        self.logger = getLogger(name)
        self.logger.setLevel(self.level)

        handler = FileHandler(self.filename)
        handler.setLevel(self.level)
        handler.setFormatter(Formatter(self.fmt))

        self.logger.addHandler(handler)

    def info(self, msg, *args):
        if len(args) != 0:
            s = "".join(str(x) for x in args)
            msg = msg + s

        self.logger.info(msg)
