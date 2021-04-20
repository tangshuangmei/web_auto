"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:test_users_feedback
@time:2021/4/16 9:28
@desc:
"""
import pytest
import time

class TestUsersFeedback():
    @pytest.fixture(autouse=True)
    def open(self, usersFeedbackiframePage):
        usersFeedbackiframePage.open("/users/feedbackiframe/")
        # 切换iframe
        usersFeedbackiframePage.to_iframe()

    def test_feedback_1(self, usersFeedbackiframePage):
        """意见反馈-反馈类型有三个下拉选项：改进建议、页面布局、提BUG """
        all_options = usersFeedbackiframePage.all_subjects()
        print("获取到所有的选项", str(all_options))
        assert all_options == ["改进建议", "页面布局", "提BUG"]

    def test_feedback_2(self, usersFeedbackiframePage):
        """意见反馈-反馈类型选页面布局，被选中：页面布局"""
        # 1.选页面布局
        usersFeedbackiframePage.select_subject(value="页面布局")
        assert usersFeedbackiframePage.selected_subject() == "页面布局"
        # 2.选提bug
        usersFeedbackiframePage.select_subject(value="提BUG")
        assert usersFeedbackiframePage.selected_subject() == "提BUG"
        # 3.改进建议
        usersFeedbackiframePage.select_subject(value="改进建议")
        assert usersFeedbackiframePage.selected_subject() == "改进建议"

    @pytest.mark.parametrize("test_input", ["改进建议", "页面布局", "提BUG"])
    def test_feedback_select(self, usersFeedbackiframePage, test_input):
        """意见反馈-反馈类型选页面布局，被选中：页面布局"""
        # 参数化
        usersFeedbackiframePage.select_subject(value=test_input)
        assert usersFeedbackiframePage.selected_subject() == test_input

    def test_feedback_send(self, usersFeedbackiframePage):
        """意见反馈，反馈类型：改进建议，反馈内容为空，联系方式为空
        点send按钮，alert弹窗提示：提交成功！"""
        # 1.反馈类型：改进建议
        usersFeedbackiframePage.select_subject(value="改进建议")
        # 2.反馈内容
        usersFeedbackiframePage.input_textarea("")
        # 3.联系方式
        usersFeedbackiframePage.input_feedback_email("")
        # 4.点send按钮
        usersFeedbackiframePage.click_send_btn()
        # 获取alert结果并断言
        text = usersFeedbackiframePage.get_alert_text()
        assert text == "提交成功！"

    @pytest.mark.parametrize("test_input,expected",[
        [{"subject":"改进建议","textarea":"","email":""},"提交成功！"],
        [{"subject": "改进建议", "textarea": "测试内容test", "email": ""}, "提交成功！"],
        [{"subject": "改进建议", "textarea": "", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "改进建议", "textarea": "测试内容test", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "页面布局", "textarea": "", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "提BUG", "textarea": "", "email": "1111@qq.com"}, "提交成功！"],
    ])
    def test_feedback_send_params(self, usersFeedbackiframePage, test_input, expected):
        """意见反馈，参数化，alert弹窗提示：提交成功！"""
        # 1.反馈类型
        usersFeedbackiframePage.select_subject(value=test_input["subject"])
        # 2.反馈内容
        usersFeedbackiframePage.input_textarea(test_input["textarea"])
        # 3.联系方式
        usersFeedbackiframePage.input_feedback_email(test_input["email"])
        # 4.点send按钮
        usersFeedbackiframePage.click_send_btn()
        # 获取alert结果并断言
        text = usersFeedbackiframePage.get_alert_text()
        assert text == expected




