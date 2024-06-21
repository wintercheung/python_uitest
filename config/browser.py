#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午12:46

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def browser_options():
    """
    浏览器的相关配置
    :return: 配置 options
    """
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


def open_browser(brower_type):
    """
    打开浏览器
    :param brower_type:
    :return:
    """
    browser = {'chrome': ['Chrome', 'chrome', 'cc', '谷歌'],
               'ie': ['ie', 'Ie', 'IE']}
    if brower_type in browser['chrome']:
        driver = webdriver.Chrome(options=browser_options())
    elif brower_type in browser['ie']:
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
