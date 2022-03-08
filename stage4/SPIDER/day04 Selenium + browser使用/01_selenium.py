# 导入selenium的webdriver接口，因为webdriver接口集成了打开浏览器的驱动
from selenium import webdriver

# 1. 打开Chrome浏览器
driver = webdriver.Chrome()  # 创建了一个浏览器对象，真正的打开了浏览器

# 2. 在浏览器的地址栏输入百度的url地址，并确认
driver.get('http://www.baidu.com/')
# 3. 浏览器窗口最大化
driver.maximize_window()
# 4. 获取屏幕快照，即快速照一张相
driver.save_screenshot(
    'baidu.png')  # UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
# 说明了selenium已经弃用了phantomjs，可以使用chrome或firefox的无界面模式
# 5. find()方法
print(driver.page_source.find('aaaaaaaaaaaaa'))
# 6. 关闭浏览器
driver.quit()
