#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午1:28

import openpyxl

from keys.ui_keys import Keys
from config import excel_result

def parse(value):
    """
    解析测试用例中测试参数单元格的内容，并转换为字典的形态返回
    :param value:
    :return: 字典格式的用例信息
    """
    data = dict()
    if value:
        str_temp = value.split(';')  # 按照分号切分 value
        for temp in str_temp:
            t = temp.split('=', 1)
            data[t[0]] = t[1]
    else:
        pass
    return data


def read(file, log):
    """
    获取指定的测试用例文件，进行自动化执行
    :param file:
    :param log:
    :return:
    """
    excel = openpyxl.load_workbook(file)
    # 获取所有的sheet页，来执行里面的测试内容
    for name in excel.sheetnames:
        sheet = excel[name]
        log.info('*****************正在执行{}Sheet页*****************'.format(name))
        for values in sheet.values:
            # 获取测试用例的正文内容
            if type(values[0]) is int:
                # 用例描述可以用于日志的输出
                log.info('*****************正在执行：{}*****************'.format(values[3]))
                # 参数最终形态：'brower_type=Chrome' 改变为 {brower_type: 'Chrome'}
                data = parse(values[2])
                # 实例化操作
                if values[1] == 'open_browser':
                    key = Keys(**data)
                # 断言行为:基于断言的返回结果来判定测试的成功失败，并进行写入操作
                elif 'assert' in values[1]:
                    status = getattr(key, values[1])(expected=values[4], **data)
                    # 基于status判定写入的测试结果
                    if status:
                        excel_result.write_pass(sheet.cell, row=values[0] + 2, column=6)
                    else:
                        excel_result.write_fail(sheet.cell, row=values[0] + 2, column=6)
                    # 保存Excel：放在这里以确保每一次写入都可以被保存，避免因为代码报错而未保存之前的测试结果
                    excel.save(file)
                else:
                    getattr(key, values[1])(**data)
    excel.close()
    log.info('*****************Excel解析执行完毕*****************')
