"""
@author:tangshuangmei
@contact:tang.shuangmei@trs.com.cn
@file:test_login
@time:2021/4/16 17:37
@desc:
"""
import pytest
import allure


def login(username,password):
    '''登录'''
    print("输入账号：%s"%username)
    print("输入密码：%s"%password)
    # 返回
    return{"code":0,"msg":"success"}
test_data = [
        ({"username":"yoyo1","password":"123456"}, "success", "1341输入正确的账号，正确的密码，登陆成功"),
        ({"username": "yoyo2", "password": "123456"}, "fail", "56642输入正确的账号，错误的面膜，登陆失败"),
        ({"username": "yoyo3", "password": "123456"}, "success", "687输入正确的账号，正确的密码，登陆成功"),
    ]
@allure.story("登陆的案例")
@allure.title("用例的标题:{title}")
@pytest.mark.parametrize("test_input,expected,title", test_data)
def test_login(test_input,expected, title):
    actual_result = login(test_input["username"],test_input["password"])
    assert actual_result["msg"] == expected