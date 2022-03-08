"""
    使用selenium模拟登录qq邮箱
"""
from selenium import webdriver

# 1. 打开浏览器并进入登录页
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
driver.minimize_window()

driver.find_element_by_id('qqLoginTab').click()

# 2. 切换iframe子页面：因为selenium默认支持id或者name两个属性值的切换
driver.switch_to.frame('login_frame')

# 3. 用户名 + 密码 + 登录按钮
driver.find_element_by_xpath('//*[@id="u"]').send_keys('2131354496@qq.com')
driver.find_element_by_class_name('inputstyle.password').send_keys('worinima234')
driver.find_element_by_xpath('//*[@id="login_button"]').click()
