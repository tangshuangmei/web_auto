"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:test_register
@time:2021/4/14 17:57
@desc:
"""
from pages1.register_page import RegisterPage
import pytest


@pytest.fixture()
def delete_user(db):
    sql = 'DELETE FROM users_userprofile WHERE username = "12390@qq.com";'
    db.execute(sql)


class TestRegister():

    @pytest.fixture(autouse=True)
    def open_register(self, registerPage):
        registerPage.open("/users/register/")

    def test_register_success(self, registerPage, delete_user):
        '''测试注册成 数据清理账号'''
        registerPage.input_email("12390@qq.com")
        registerPage.input_password("123456")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.register_success_text()
        # 断言
        assert actual_result == "尊敬的用户，您好，账户已激活成功！"


    def test_email_1(self, registerPage):
        '''注册-输入邮箱为空，密码为空，
        点提交按钮，邮箱输入框红色提示'''
        # registerPage.open("/users/register/")
        registerPage.input_email("")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_email_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput " in actual_result

    def test_email_2(self, registerPage):
        '''注册-输入邮箱格式不正确，密码为空，
        点提交按钮，邮箱输入框红色提示'''
        # registerPage.open("/users/register/")
        registerPage.input_email("1234")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_email_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput " in actual_result

    def test_password_3(self, registerPage):
        '''注册-邮箱格式正确（111@qq.com），密码为空,
        点提交按钮，密码输入框红色提示'''
        # registerPage.open("/users/register/")
        registerPage.input_email("111@qq.com")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput " in actual_result

    def test_password_4(self, registerPage):
        '''注册-邮箱格式正确（111@qq.com），密码小于6位,
        点提交按钮，密码输入框红色提示'''
        # registerPage.open("/users/register/")
        registerPage.input_email("111@qq.com")
        registerPage.input_password("12345")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput " in actual_result

    def test_password_5(self, registerPage):
        '''注册-邮箱格式正确（111@qq.com），密码大于20位,
        点提交按钮，密码输入框红色提示'''
        # registerPage.open("/users/register/")
        registerPage.input_email("111@qq.com")
        registerPage.input_password("123456789012345678901")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput " in actual_result

    def test_email_input_6(self, registerPage):
        '''注册-邮箱输入框，输入文本：111@qq.com，再清空文本，输入框为空'''
        registerPage.input_email("111@qq.com")
        assert registerPage.get_email_attr(attr="value") == "111@qq.com"
        # 清空输入框
        registerPage.clear_email()
        assert registerPage.get_email_attr(attr="value") == ""

    def test_password_input_7(self,registerPage):
        '''注册-密码输入框输入文本：123456，显示******'''
        registerPage.input_password("123456")
        assert registerPage.get_password_attr(attr="value") == "123456"
        # 判断输入框显示****
        assert registerPage.get_password_attr(attr="type") == "password"

    def test_register_link_8(self, registerPage, base_url):
        '''注册-点页面“回到首页”按钮，点击跳转到首页'''
        link = registerPage.get_link_href('//*[@class="index-font"]')
        print("实际结果：%s"%link)
        assert link == base_url+"/"

    def test_register_link_9(self, registerPage, base_url):
        '''注册-点页面“logo图片”按钮，点击跳转到首页'''
        link = registerPage.get_link_href('//*[@class="index-logo"]')
        print("实际结果：%s" % link)
        assert link == base_url + "/"

    def test_register_link_10(self, registerPage, base_url):
        '''注册-点页面“登录”按钮，点击跳转到登陆页面'''
        link = registerPage.get_link_href('//*[text()="[登录]"]')
        print("实际结果：%s" % link)
        assert link == base_url + "/users/login/"

    def test_register_link_11(self, registerPage, base_url):
        '''注册-点页面“注册”按钮，点击跳转到注册页面'''
        link = registerPage.get_link_href('//*[text()="[注册]"]')
        print("实际结果：%s" % link)
        assert link == base_url + "/users/register/"

    def test_register_link_12(self, registerPage, base_url):
        '''注册-点页面“立即登录”按钮，点击跳转到登陆页面'''
        link = registerPage.get_link_href('//*[text()="[立即登录]"]')
        print("实际结果：%s" % link)
        assert link == base_url + "/users/login/"