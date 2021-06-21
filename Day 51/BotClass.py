from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time
import os

TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')

PROMISED_UP = 100
PROMISED_DOWN = 80
SERVICE_PROVIDER = 'JioCare'

SPEEDTEST_URL = 'https://www.speedtest.net/'


class InternetSpeedTwitterBot:
    
    
    def __init__(self):
        self.up = None
        self.down = None
        self.resultid = None
        options = EdgeOptions()
        options.use_chromium = True
        self.driver = Edge(options = options)
    
    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        time.sleep(5)
        start = self.driver.find_element_css_selector(".js-start-test")
        start.click()
        
        time.sleep(60)
        self.up = int(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.down = int(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.resultid = SPEEDTEST_URL + self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').getAttribute('href')
        self.driver.quit()
    
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(5)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey @{SERVICE_PROVIDER}\n Why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?\n{self.resultid}"
        tweet_compose.send_keys(tweet)
        time.sleep(5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(5)
        self.driver.quit()
