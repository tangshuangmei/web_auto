"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:users_login_page
@time:2021/4/15 17:00
@desc:
"""
from common1.base import Base


class UsersLoginPage(Base):
    login_username_loc = ("id", "username")
    login_password_loc = ("id", "password_l")
    login_btn_loc = ("id", "jsLoginBtn")
    error_tips_loc = ("class name", "errorlist")
    tips_loc = ("id", "jsLoginTips")

    def input_login_username(self, user=""):
        '''输入登陆用户名'''
        self.send(self.login_username_loc, user)

    def input_login_password(self, password=""):
        '''输入密码'''
        self.send(self.login_password_loc, password)

    def click_login_btn(self):
        '''点击登录按钮'''
        self.click(self.login_btn_loc)

    def get_error_tips(self):
        '''获取页面提示语'''
        tips = self.get_text(self.error_tips_loc)
        if not tips:
            tips = self.get_text(self.tips_loc)
        return tips



