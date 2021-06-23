from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import random

INSTA_EMAIL = os.environ.get('INSTA_EMAIL')
INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD')
SIMILAR_ACCOUNT = 'meme_coding'

class InstaFollower:
    
    
    def __init__(self):
        options = EdgeOptions()
        options.use_chromium = True
        self.driver = Edge(options = options)
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys(INSTA_EMAIL)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login.send_keys(INSTA_PASSWORD)
        button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        button.click()
    
    def find_and_follow_followers_list(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}')
        time.sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)
            try:
                follow_btns = self.driver.find_elements_by_css_selector('.PZuss button')
                for btn in follow_btns:
                    if btn.text == 'Follow':
                        time.sleep(1)
                        btn.click()
                        rand_time = random.randint(2, 40)
                        time.sleep(rand_time)
            except NoSuchElementException:
                break
    
    def logout(self):
        profile_img = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
        profile_img.click()
        time.sleep(1)
        log_out = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div')
        log_out.click()
        self.driver.quit()
