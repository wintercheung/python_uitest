#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午12:56

from logging import config


def get_logger(name):
    """
    获取日志配置
    :param name: 日志配置文件名
    :return: 加载配置
    """
    config.fileConfig(name, disable_existing_loggers=False)
    return get_logger()