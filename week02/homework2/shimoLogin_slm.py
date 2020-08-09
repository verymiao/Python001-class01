from selenium import webdriver
import time

url = 'https://shimo.im/welcome'
userName='23237683@qq.com'
passWord='23237683'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    #进入登陆页面
    browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()
    time.sleep(3) #防止网络超时

    #输入用户名密码,登陆
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(userName)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(passWord)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    #输出登陆成功页面
    time.sleep(1)
    print(browser.page_source)

except Exception as error:
    print(error)

finally:
    time.sleep(5)
    browser.close()