#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : winter cheung
# @Time    : 2024/6/21 下午12:39

import time

from selenium.webdriver.support.wait import WebDriverWait

from config import browser


class Keys:
    """
    关键字驱动类：封装基本元素的操作方法
    """

    def __init__(self, brower_type):
        self.driver = browser.open_browser(brower_type)
        self.driver.implicitly_wait(5)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => false
                })
              """
        })

    def open(self, url):
        """
        访问 url
        :param url:
        :return:
        """
        self.driver.get(url)

    def locate(self, by, value):
        """
        元素定位
        :param by:
        :param value:
        :return:
        """
        return self.driver.find_element(by, value)

    def input(self, by, value, txt):
        """
        输入操作
        :param by:
        :param value:
        :param txt:
        :return:
        """
        self.locate(by, value).send_keys(txt)

    def click(self, by, value):
        """
        点击操作
        :param by:
        :param value:
        :return:
        """
        self.locate(by, value).click()

    def quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def driver_wait(self, by, value):
        """
        显示等待
        :param by:
        :param value:
        :return:
        """
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(by, value),
                                                         message='元素获取失败')

    def sleep(self, wait_time):
        """
        强制等待
        :param wait_time:
        :return:
        """
        time.sleep(int(wait_time))

    def switch_handle(self, status=1):
        """
        句柄切换
        :param status:
        :return:
        """
        handles = self.driver.window_handles
        if status == 1:
            self.driver.close()
        self.driver.switch_to.window(handles[1])

    def assert_almost_equal(self, by, value, expected):
        """
        断言预期结果是否包含在实际结果内
        :param by:
        :param value:
        :param expected:
        :return:
        """
        try:
            reality = self.locate(by, value).text
            assert expected in reality, '{0}不在{1}的范围内'.format(expected, reality)
            return True
        except:
            return False

    def assert_text(self, by, value, expected):
        """
        断言文本
        :param by:
        :param value:
        :param expected:
        :return:
        """
        try:
            reality = self.locate(by, value).text
            assert expected == reality, '{0}与{1}不相等'.format(expected, reality)
        except Exception as e:
            print('断言失败：{}'.format(e))

    def switch_frame(self, value, by=None):
        """
        切换Iframe
        :param value:
        :param by:
        :return:
        """
        if by is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate(by, value))
