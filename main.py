#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午2:02

import os

from config import log
from tools.read_files import read

if __name__ == '__main__':
    # 创建log对象
    log = log.get_logger(name="./config/log.ini")
    # 通过读取data路径下是否有测试用例(PS:有，就执行，没有就不执行)
    # 测试用例集合
    cases = list()
    # 读取路径下的测试用例
    for path, dir, files in os.walk('./data/'):
        for file in files:
            # 获取文件的后缀名
            file_type = os.path.splitext(file)[1]
            file_name = os.path.splitext(file)[0]
            if file_type == '.xlsx':
                case_path = path + file
                cases.append(case_path)
            else:
                log.error('*****************文件类型错误：{}*****************'.format(file))
    for case in cases:
        log.info('*****************正在执行{}文件*****************'.format(case))
        read(case, log)