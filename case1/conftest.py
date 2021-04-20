"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:conftest
@time:2021/4/14 17:58
@desc:
"""
import os

import allure
import pytest
from selenium import webdriver
from pages1.register_page import RegisterPage
from common1.connct_mysql import DbConnect, dbinfo
from pages1.users_login_page import UsersLoginPage
from pages1.users_feedbackiframe_page import UsersFeedbackiframePage
from pages1.users_userinfo_page import UserUserinfoPage


@pytest.fixture(scope="session", name="driver")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # quit退出浏览器
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    url = "http://49.235.92.12:8200"
    return url


@pytest.fixture(scope="session")
def registerPage(driver, base_url):
    register = RegisterPage(driver, base_url)
    return register


@pytest.fixture(scope="session")
def db():
    _db = DbConnect(dbinfo, "online")
    yield _db
    _db.close()


@pytest.fixture(scope="session")
def usersLoginPage(driver, base_url):
    userLogin = UsersLoginPage(driver, base_url)
    return userLogin


@pytest.fixture(scope="session")
def usersFeedbackiframePage(driver, base_url):
    feedback = UsersFeedbackiframePage(driver, base_url)
    return feedback


@pytest.fixture(scope="session")
def login_driver(driver, usersLoginPage: UsersLoginPage):
    """用户登录，返回dirver"""
    usersLoginPage.open("/users/login/")
    usersLoginPage.input_login_username("12345678@qq.com")
    usersLoginPage.input_login_password("12345678")
    usersLoginPage.click_login_btn()
    return driver


@pytest.fixture(scope="session")
def userInfoPage(login_driver, base_url):
    """需要先登录，返回已登录的页面对象"""
    userInfo = UserUserinfoPage(login_driver, base_url)
    return userInfo


# _driver = None
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#     获取每个用例状态的钩子函数
#     :param item:
#     :param call:
#     :return:
#     '''
#     # 获取钩子方法的调用结果
#     outcome = yield
#     rep = outcome.get_result()
#     # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         # 添加allure报告截图
#         if hasattr(_driver, "get_screenshot_as_png"):
#             with allure.step('添加失败截图...'):
#                 allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
#
#
# @pytest.fixture(scope='session')
# def browser():
#     global _driver
#     if _driver is None:
#         _driver = webdriver.Chrome()
#     yield _driver
#     print("1111111111")
#     _driver.quit()
