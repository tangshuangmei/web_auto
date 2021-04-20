"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:test_users_login
@time:2021/4/15 17:18
@desc:
"""
import pytest
from pages1.users_login_page import UsersLoginPage


class TestUsersLogin():

    @pytest.fixture(autouse=True)
    def open_login(self, usersLoginPage):
        usersLoginPage.open("/users/login/")

    def test_login_1(self, usersLoginPage):
        '''登录-输入用户名为空，任意密码123456，点击登录按钮，提示“这个字段是必须的”'''
        usersLoginPage.input_login_username("")
        usersLoginPage.input_login_password("123456")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == "这个字段是必须的"

    def test_login_2(self, usersLoginPage):
        '''登录-输入邮箱格式不正确"123abc"，密码123456，点击登录按钮，提示“用户名或密码错误”'''
        usersLoginPage.input_login_username("123abc")
        usersLoginPage.input_login_password("123456")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == "用户名或密码错误"

    def test_login_3(self, usersLoginPage):
        '''登录-输入邮箱格式正确"12345678@qq.com"，密码不正确”123abc“，点击登录按钮，提示“用户名或密码错误”'''
        usersLoginPage.input_login_username("12345678@qq.com")
        usersLoginPage.input_login_password("123abc")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == "用户名或密码错误"

    def test_login_4(self, usersLoginPage,base_url):
        '''登录-输入邮箱格式正确"12345678@qq.com"，密码正确”12345678“，点击登录按钮，登陆成功'''
        usersLoginPage.input_login_username("12345678@qq.com")
        usersLoginPage.input_login_password("12345678")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == ""
        # 通过跳转的url地址判断
        url = usersLoginPage.driver.current_url
        print("获取跳转后的url", url)
        assert url == base_url+"/"


