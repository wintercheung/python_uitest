#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午12:46

from selenium import webdriver


def browser_options():
    # 创建 chrome 的配置项
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"  # 页面加载策略
    options.add_argument('window-position=2500,200')  # 指定位置启动浏览器
    options.add_argument('window-size=1200,800')  # 设置窗体的启动大小

    # 去掉账号密码弹出框
    prefs = dict()
    prefs['credentials_enable_service'] = False
    prefs['profile.password_manager_enable'] = False
    options.add_experimental_option('prefs', prefs)

    # 去掉控制台多余信息
    options.add_argument('--log_level=3')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 去掉控制台多余信息

    return options