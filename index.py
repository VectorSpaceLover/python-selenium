from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser
import time
import os
import json

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
opt.add_argument('--new-window')
TIMEOUT = 2

class ScrapBot:
    def __init__(self):
        self.base_url = 'https://omd.infomc.biz/iPC/login'
    def login(self):
        driver = webdriver.Chrome(chrome_options=opt, executable_path="chromedriver.exe")
        driver.implicitly_wait(5)
        self.driver = driver

        driver.get(self.base_url)
        driver.implicitly_wait(1)

        driver.find_element_by_xpath('//input[@id="txtUserName"]').send_keys('James11009')
        driver.find_element_by_xpath('//input[@id="txtPassword"]').send_keys('987Qwer!')
        driver.find_element_by_xpath('//button[@type="submit"]').click()

        time.sleep(20)
    def catch_info(self):
        rect_list = self.driver.find_elements_by_xpath('//g//rect')

        for i in range(0, len(rect_list)):
            action = ActionChains(self.driver)
            action.move_to_element(rect_list[i])
            action.click(on_element = rect_list[i])
            action.perform()
            txt = self.driver.find_element_by_xpath('//div[@id="panelClaims"]//div[@aria-hidden="true"]').getText()
            print(txt)
if __name__ == '__main__':
    scrapBot = ScrapBot()
    scrapBot.login()
    scrapBot.catch_info()
