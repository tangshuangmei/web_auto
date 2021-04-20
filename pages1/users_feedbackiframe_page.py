"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:users_feedbackiframe_page
@time:2021/4/16 9:06
@desc:
"""

from common1.base import Base


class UsersFeedbackiframePage(Base):
    '''意见反馈页面'''
    iframe_loc = ("id", "feedback_iframe")
    select_loc = ("name", "subject")
    textarea_loc = ("id", "message")
    email_loc = ("name", "email")
    send_btn_loc = ("class name", "button")

    def to_iframe(self):
        '''切换到iframe页面'''
        self.switch_iframe(self.iframe_loc)

    def select_subject(self, value=""):
        '''选中下拉选项'''
        self.select_by_value(self.select_loc, value)

    def all_subjects(self):
        '''获取所有的选项'''
        all_options = self.select_object(self.select_loc).options
        all_text = [i.text for i in all_options]
        return all_text

    def selected_subject(self):
        '''获取选中选项'''
        selected = self.select_object(self.select_loc).first_selected_option
        return selected.text

    def input_textarea(self, text=""):
        '''输入反馈内容'''
        self.send(self.textarea_loc, text)

    def input_feedback_email(self, email=""):
        '''输入联系方式'''
        self.send(self.email_loc, email)

    def click_send_btn(self):
        '''点send按钮'''
        self.click(self.send_btn_loc)





