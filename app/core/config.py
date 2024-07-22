# app/base/config.py

import configparser

class Config:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, option):
        return self.config.get(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)

    def getfloat(self, section, option):
        return self.config.getfloat(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)

    def sections(self):
        return self.config.sections()

# 创建一个全局配置对象，以便在其他地方使用
config = Config()