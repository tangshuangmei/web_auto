"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:test_users_info
@time:2021/4/16 11:28
@desc:
"""
import pytest


class TestUsersInfo():

    @pytest.fixture(autouse=True)
    def open(self, userInfoPage):
        """直接进入到个人资料页面"""
        userInfoPage.open("/users/userinfo/")

    def test_info_1(self, userInfoPage):
        """修改个人信息-输入昵称为空，点击保存按钮"""
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name(name="")
        userInfoPage.click_save_btn()
        assert userInfoPage.get_error_tips() == "请输入昵称！"

    @pytest.mark.parametrize("test_input", ["土土", "Smith"])
    def test_info_2(self, userInfoPage, test_input):
        """修改个人信息-修改昵称：土土，点击保存按钮，提示个人信息修改成功！"""
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name(name=test_input)
        userInfoPage.click_save_btn()
        assert userInfoPage.get_dialog_text() == "个人信息修改成功！"
        assert userInfoPage.get_nick_value() == test_input

    def test_info_3(self, userInfoPage):
        """修改个人信息-修改昵称：smithabcdef，大于10个字符，输入框只显示10个字符"""
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name(name="smithabcdef")
        assert userInfoPage.get_nick_value() == "smithabcde"


