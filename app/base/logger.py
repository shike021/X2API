# app/base/logger.py

import logging
import os
import sys
import logging.handlers

# 全局日志配置
def configure_logging(log_level=logging.INFO,
                      log_file='app.log',
                      log_dir='./logs',
                      max_bytes=1024 * 1024 * 5,
                      backup_count=20):

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # 创建日志文件处理器
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, log_file),
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    file_handler.setLevel(log_level)

    # Create a stream handler for console logging
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(log_level)

    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # 添加到root logger
    if not root_logger.hasHandlers():
        root_logger.addHandler(file_handler)
        root_logger.addHandler(stream_handler)

# 为模块提供获取logger的函数
def get_module_logger(module_name):
    logger = logging.getLogger(module_name)
    return logger

# 导入时调用
configure_logging()