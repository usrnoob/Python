
# \n  换行
# \t  tab，可以当成是缩进
# \  反斜杠
# \’  单引号，可以在单引号字符串中打印出单引号
# \”  双引号，可以在双引号字符串中打印出双引号



# python中3个引号开头的字符串中可以包含多行文本
my_str="""
this is the first line
this is the second line
this is the last line
"""



test_scenario = "登录场景\n"
test_case_name = "\t正常登录: \n"

# two tabs
tt = "\t\t"

test_step = f"{tt}1.打开chrome浏览器\n{tt}2.输入www.itest.info\n{tt}3.在登录表单中输入用户名:example，密码:example\n{tt}4.登记登录按钮\n"

test_assert = f"{tt}应该跳转到www.itest.info/login_success页面，并出现\"登录成功\"的提示"

print(test_scenario + test_case_name + test_step + test_assert)

test_login_failed = """
        密码错误:
                1.打开chrome浏览器
                2.输入www.itest.info
                3.在登录表单中输入用户名:example，密码:incorrect
                4.登记登录按钮
                页面不发生跳转，并出现\"登录失败\"的提示
"""
print(test_login_failed)