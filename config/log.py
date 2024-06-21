#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午12:56

from logging import config

def get_logger(name):
    config.fileConfig(name, disable_existing_loggers=False)
    return get_logger()